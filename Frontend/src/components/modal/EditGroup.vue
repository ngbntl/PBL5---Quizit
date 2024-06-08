<template>
    <!-- <a-button type="primary" @click="showModal">Open Modal</a-button> -->
    <button type="primary" @click="showModal" class="flex items-end justify-end">
        <svg class="feather feather-edit" fill="none" height="24" stroke="currentColor" stroke-linecap="round"
            stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
            <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7" />
            <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z" />
        </svg></button>

    <a-modal v-model:open="open" title="Chỉnh sửa nhóm" @ok="handleOk">
        <template #footer>
            <a-button key="back" @click="handleCancel">Hủy</a-button>
            <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Xác nhận</a-button>
        </template>


        <div class="flex items-center p-4">
            <label class="w-1/3 mb-2">Tên nhóm: </label>
            <input type="text" v-model="group.name"
                class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                placeholder="Nhập tên nhóm" />
        </div>
        <div class="flex items-center p-4">
            <label class="w-1/3 mb-2">Ẩn nhóm: </label>
            <input type="checkbox" v-model="isHidden"
                class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                placeholder="Nhập tên nhóm" />


        </div>
        <label class="w-1/3  mx-4">Ảnh nhóm: </label>


        <div class="mt-3" style="display: flex; overflow-x: auto;">

            <div v-for="(img,index) in images" :key="index" style="flex: 0 0 auto;">
                <img :src="'http://localhost:4444/static/'+ formattedImagePath(img)"
                    :class="`rounded-md w-32 h-32 text-center hover:cursor-pointer mx-2 ${selectedImages === img ? 'border-4 border-blue-500' : ''}`"
                    @click="selectedImages = img">
            </div>
        </div>
    </a-modal>
</template>

<script>
import { ref, computed } from 'vue';
import { useTeacherStore } from '../../stores/modules/teacher';
export default {
    props: {
        group: {
            type: Object,
            required: true
        }
    },
    setup() {
        const teacherStore = useTeacherStore();
        const images = ref([]);
        const open = ref(false);
        const selectedImages = ref('');



        const showModal = async () => {
            images.value = await teacherStore.getImageGroups();
            open.value = true;
        };
        const handleOk = () => {
            console.log(selectedImages.value);
            open.value = false;
        };

        const handleCancel = () => {
            open.value = false;
        };
        const formattedImagePath = computed(() => {
            return img => img.replace(/\\/g, '/');
        });
        return {
            open,
            showModal,
            handleOk,
            handleCancel,

            selectedImages,
            formattedImagePath,
            images
        }
    }
}
</script>

<style>

    </style>