<template>
    <h1 class="text-3xl flex justify-center items-center mt-10 font-semibold">Kết quả thi</h1>
    <div class="p-20 items-center justify-center w-full h-screen">
        <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
                <tr>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">STT</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Họ và tên
                    </th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Trạng
                        thái</th>
                    <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Điểm</th>
                </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="(item, index) in data" :key="item.student.id">
                    <td class="px-6 py-4 whitespace-nowrap">{{ index + 1 }}</td>
                    <td class="px-6 py-4 whitespace-nowrap">{{ item.student.name }}</td>
                    <td class="px-6 py-4 whitespace-nowrap" :class="{
                            'text-green-500': item.state === 'DISCONNECTED', 
                            'text-yellow-500': item.state === 'WORKING'
                        }">
                        {{ item.state === 'DISCONNECTED' ? 'Đã hoàn thành' : (item.state === 'WORKING' ? 'Đang làm' :
                        'Đã hoàn thành') }}
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap">{{ item.score }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";
import { useStudentStore } from '../../../stores/modules/student'
import teacher from '../../../apis/modules/teacher';
import { useTeacherStore } from '../../../stores/modules/teacher';


export default {

    setup() {


        const data = ref([]);
        const route = useRoute();
        const webSocket = () => {
            data.value = useTeacherStore().getGroupTests(route.params.testId)
            const WS = ref(new WebSocket(`ws://localhost:4444/teacher`));

            WS.value.onopen = (event) => {
                console.log("Connection opened", event);

                let token = localStorage.getItem("token");

                let auth = {
                    command: "AUTHENTICATE",
                    detail: {
                        token: token,
                    },
                };
                WS.value.send(JSON.stringify(auth));

                WS.value.onmessage = (event) => {
                    let receivedData = JSON.parse(event.data);
                    if (receivedData.message == "Authenticated") {
                        console.log(route.params)
                        let join = {
                            command: "JOIN GROUP TEST",
                            detail: {
                                group_test_id: route.params.testId,
                            }
                        }
                        WS.value.send(JSON.stringify(join));
                        WS.value.onmessage = (event) => {
                            let receivedData = JSON.parse(event.data)
                            console.log(receivedData)


                            if (Array.isArray(receivedData)) {
                                data.value = receivedData;
                            }
                        }
                    }
                };
            }
        }
        onMounted(async () => {

        });
        return {

            data,
            webSocket

        }
    }

}
</script>