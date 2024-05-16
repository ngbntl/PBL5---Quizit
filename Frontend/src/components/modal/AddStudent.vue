<template>
    <div>
        <a-button type="primary" @click="showModal">Thêm học sinh</a-button>
        <a-modal v-model:open="open" title="Thêm học sinh" @ok="handleOk">
            <template #footer>
                <a-button key="back" @click="handleCancel">Hủy</a-button>
                <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Xác nhận</a-button>
            </template>
            <div class="p-4">
                <label class="block mb-2">Tên bộ sưu tập: </label>

                <vue-tags-input v-model="tag" :tags="tags" @tags-changed="newTags => tags = newTags" />



            </div>
        </a-modal>
    </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useTeacherStore } from '../../stores/modules/teacher';
import VueTagsInput from '@johmun/vue-tags-input'
export default {
    components: { VueTagsInput },
    setup() {
        const teacherStore = useTeacherStore();
        const loading = ref(false);
        const open = ref(false);
        const collectionName = ref('');
        const collection = computed(() => ({ name: collectionName.value }));
        const tag = ref('');
        const tags = ref([]);

        const updateTags = (newTags) => {
            tags.value = newTags;
        }

        const showModal = () => {
            open.value = true;
        };

        const handleOk = async () => {
            loading.value = true;
            addCollection(collection.value)

            setTimeout(() => {
                loading.value = false;
                open.value = false;
            }, 2000);
        };

        const addCollection = async (name) => {
            const result = await teacherStore.addCollection(name);
            collectionName.value = result;
            open.value = false;
        };

        const handleCancel = () => {
            open.value = false;
        };

        return {
            open,
            loading,
            collectionName,
            collection,
            tag,
            tags,
            updateTags,
            showModal,
            handleOk,
            handleCancel,
            addCollection
        };
    }
}
</script>