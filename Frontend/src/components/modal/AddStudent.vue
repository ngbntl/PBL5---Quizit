<template>
    <div>
        <a-button type="primary" @click="showModal">Thêm học sinh</a-button>
        <a-modal v-model:open="open" title="Thêm học sinh" @ok="handleOk">
            <template #footer>
                <a-button key="back" @click="handleCancel">Hủy</a-button>
                <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Xác nhận</a-button>
            </template>
            <div class="p-4">
                <label class="block mb-2">Email: </label>

                <vue3-tags-input :tags="tags" placeholder="nhập email..." @on-tags-changed="handleChangeTag" />



            </div>
        </a-modal>
    </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useTeacherStore } from '../../stores/modules/teacher';
import Vue3TagsInput from 'vue3-tags-input';
export default {
    components: { Vue3TagsInput },
    setup() {
        const teacherStore = useTeacherStore();
        const loading = ref(false);
        const open = ref(false);



        const tags = ref([]);

        const updateTags = (newTags) => {
            tags.value = newTags;
        }

        const showModal = () => {
            open.value = true;
        };

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


            tags,
            updateTags,
            showModal,
            handleOk,
            handleCancel,

        };
    }
}
</script>