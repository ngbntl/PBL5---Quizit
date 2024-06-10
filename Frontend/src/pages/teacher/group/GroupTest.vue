<template>
    <div>
        <button @click="$router.go(-1)" class=" relative ml-10 top-10">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
        </button>
        <h1 class="text-3xl flex justify-center items-center mt-10 font-semibold">
            Trạng thái làm bài
        </h1>
        <div class="p-20 items-center justify-center w-full h-screen">
            <table class="min-w-full divide-y divide-gray-200">
                <thead class="bg-gray-50">
                    <tr>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            STT
                        </th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Họ và tên
                        </th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Trạng thái
                        </th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Điểm
                        </th>
                        <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                            Số lần vi phạm
                        </th>
                    </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                    <tr v-for="(item, index) in data" :key="item.student.id" @click="getTest(item)">
                        <td class="px-6 py-4 whitespace-nowrap">{{ index + 1 }}</td>
                        <td class="px-6 py-4 whitespace-nowrap">{{ item.student.name }}</td>
                        <td class="px-6 py-4 whitespace-nowrap" :class="{
              'text-green-500': item.start != null && item.end !=null,
              'text-yellow-500': item.start != null && item.end == null ,
            }">
                            {{
                            item.start === null
                            ? "Chưa tham gia"
                            : (item.start != null && item.end == null)
                            ? "Đang làm bài"
                            : "Đã hoàn thành"
                            }}
                        </td>
                        <td class="px-6 py-4 whitespace-nowrap">{{ item.score*10 }}</td>
                        <td class="px-6 py-4 whitespace-nowrap">{{ item.violate }}</td>

                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
<script>
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";

import { useTeacherStore } from "../../../stores/modules/teacher";

export default {
    setup() {
        const data = ref([]);
        const route = useRoute();
        const teacherStore = useTeacherStore();
        const webSocket = () => {

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
                        console.log(route.params);
                        let join = {
                            command: "JOIN GROUP TEST",
                            detail: {
                                group_test_id: route.params.testId,
                            },
                        };
                        WS.value.send(JSON.stringify(join));
                        WS.value.onmessage = (event) => {
                            let receivedData = JSON.parse(event.data);
                            console.log(receivedData);

                            if (Array.isArray(receivedData)) {
                                console.log(receivedData)
                            }
                        };
                    }
                };
            };
        };
        onMounted(async () => {
            data.value = await teacherStore.getStudentTest(route.params.testId);
            webSocket();
        });
        return {
            data,
            webSocket,
        };
    },
};
</script>
