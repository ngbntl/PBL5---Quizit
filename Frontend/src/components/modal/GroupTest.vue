<template>
    <div>
        <a-button type="primary" @click="showModal">Tạo bài kiểm tra</a-button>
        <a-modal v-model:open="open" title="Tạo bải kiểm tra" @ok="handleOk">
            <template #footer>
                <a-button key="back" @click="handleCancel">Hủy</a-button>
                <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Xác nhận</a-button>
            </template>

            <div class="flex items-center p-4">
                <label class="w-1/3 mb-2">Tên bài kiểm tra: </label>
                <input type="text" v-model="name"
                    class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                    placeholder="Nhập tên bài kiểm tra" />
            </div>
            <div class="flex items-center p-4">
                <label class="w-1/3 mb-2">Chọn bộ sưu tập: </label>
                <select name="" id=""
                    class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                    v-model="selectedCollection">
                    <option v-for="collection in collections" :key="collection.id" :value="collection.id">
                        {{ collection.name }}
                    </option>
                </select>
            </div>
            <div class="flex items-center p-4">
                <label class="w-1/3 mb-2">Chọn đề thi: </label>
                <select name="" id=""
                    class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                    v-model="testId">
                    <option v-for="test in tests" :key="test.id" :value="test.id">
                        {{ test.name }}
                    </option>
                </select>
            </div>
            <div class="flex items-center p-4">
                <label class="w-1/3 mb-2">Thời gian bắt đầu: </label>
                <input type="datetime-local" v-model="startTime"
                    class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline" />
            </div>
            <div class="flex items-center p-4">
                <label class="w-1/3 mb-2">Thời gian kết thúc: </label>
                <input type="datetime-local" v-model="endTime"
                    class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline" />
            </div>
            <div class="flex items-center p-4">
                <label class="w-1/3 mb-2">Thời lượng: </label>
                <input type="number" v-model="duration"
                    class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline" />
            </div>
            <div class="flex items-center p-4 ">
                <label class="w-1/3 ">Trộn đề: </label>
                <input type="checkbox" v-model="shuffle"
                    class="w-2/3 h-6 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded" />
            </div>

        </a-modal>
    </div>
</template>

<script>
import { ref, watch } from "vue";
import { useTeacherStore } from "../../stores/modules/teacher";
import Vue3TagsInput from "vue3-tags-input";
import { useRouter } from 'vue-router';
export default {
    components: { Vue3TagsInput },
    setup() {
        const formatDate = (date, format = 'YYYY-MM-DDTHH:mm:ss') => {
            const d = new Date(date);
            let month = '' + (d.getMonth() + 1);
            let day = '' + d.getDate();
            let year = d.getFullYear();
            let hour = d.getHours();
            let minute = d.getMinutes();
            let second = d.getSeconds();

            if (month.length < 2) month = '0' + month;
            if (day.length < 2) day = '0' + day;
            if (hour.length < 2) hour = '0' + hour;
            if (minute.toString().length < 2) minute = '0' + minute;
            if (second.toString().length < 2) second = '0' + second;

            return [year, month, day].join('-') + 'T' + [hour, minute, second].join(':');
        }

        const startTime = ref(formatDate(new Date()));
        const endTime = ref(formatDate(new Date()));
        const router = useRouter()
        const teacherStore = useTeacherStore();
        const loading = ref(false);
        const open = ref(false);
        const name = ref('')
        const testId = ref('')
        const collections = ref([])

        const duration = ref('')
        const shuffle = ref(false)
        const selectedCollection = ref(null)
        const tests = ref([])
        const data = ref({
            group_id: router.currentRoute.value.params.id,
            test_id: testId.value,
            name: name.value,
            start: startTime.value,
            end: endTime.value,
            duration: duration.value,
            shuffle: shuffle.value
        });

        watch([name, testId, startTime, endTime, duration, shuffle], () => {
            data.value = {
                group_id: router.currentRoute.value.params.id,
                test_id: testId.value,
                name: name.value,
                start: startTime.value,
                end: endTime.value,
                duration: duration.value,
                shuffle: shuffle.value
            };
        }, { immediate: true, deep: true });
        watch(selectedCollection, async (newCollectionId) => {
            if (newCollectionId) {
                tests.value = await teacherStore.getTests(newCollectionId);


            }
        });

        const showModal = async () => {
            open.value = true;
            collections.value = await teacherStore.getCollections();
        };


        const handleOk = async () => {
            loading.value = true;
            console.log(data.value);

            const payload = {
                ...data.value,
                start: formatDate(startTime.value),
                end: formatDate(endTime.value),
            };
            await teacherStore.addTestInGroup(payload);

            setTimeout(() => {
                loading.value = false;
                open.value = false;
            }, 2000);
        };

        const handleCancel = () => {
            open.value = false;
        };

        return {
            router,
            open,
            loading,
            tests,
            name,
            testId,
            startTime,
            endTime,
            duration,
            shuffle,
            collections,
            selectedCollection,
            formatDate,
            showModal,
            handleOk,
            handleCancel,
        };
    },
};
</script>
