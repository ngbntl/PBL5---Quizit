<template>
    <div>
        <a-button type="primary" @click="showModal">Tạo bài kiểm tra</a-button>
        <a-modal v-model:open="open" title="tạo bải kiểm tra" @ok="handleOk">
            <template #footer>
                <a-button key="back" @click="handleCancel">Hủy</a-button>
                <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Xác nhận</a-button>
            </template>
            <div class="p-4">
                <label class="block mb-2">Chọn bộ sưu tập: </label>
                <select name="" id=""
                    class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                    v-model="selectedCollection">
                    <option v-for="collection in collections" :key="collection.id" :value="collection.id">
                        {{ collection.name }}
                    </option>
                </select>
            </div>

            <div class="p-4">
                <label class="block mb-2">Chọn ngân hàng câu hỏi: </label>

                <select name="" id=""
                    class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline">
                    <option v-for="questionBank in questionBanks" :key="questionBank.id" :value="questionBank.id">
                        {{ questionBank.name }}
                    </option>
                </select>
            </div>



        </a-modal>
    </div>
</template>

<script>
import { ref, watch } from "vue";
import { useTeacherStore } from "../../stores/modules/teacher";
import Vue3TagsInput from "vue3-tags-input";
export default {
    components: { Vue3TagsInput },
    setup() {
        const teacherStore = useTeacherStore();
        const loading = ref(false);
        const open = ref(false);
        const questionBanks = ref([]);
        const collections = ref([]);
        const tags = ref([]);
        const selectedCollection = ref(null);

        const updateTags = (newTags) => {
            tags.value = newTags;
        };

        const showModal = async () => {
            open.value = true;
            collections.value = await teacherStore.getCollections();

        };
        watch(selectedCollection, async (newCollectionId) => {
            if (newCollectionId) {
                questionBanks.value = await teacherStore.getQuestionBank(newCollectionId);
            }
        });
        const handleOk = async () => {
            loading.value = true;

            setTimeout(() => {
                loading.value = false;
                open.value = false;
            }, 2000);
        };

        const handleCancel = () => {
            open.value = false;
        };

        return {
            open,
            loading,
            collections,
            selectedCollection,
            tags,
            questionBanks,
            updateTags,
            showModal,
            handleOk,
            handleCancel,
        };
    },
};
</script>
