<template>
    <div class="flex flex-col p-4">
        <h1 class="text-2xl font-bold mb-4">Thông tin cá nhân</h1>

        <div class="flex items-center mb-4">
            <img :src="avatar" alt="Avatar" class="w-24 h-24 rounded-full mr-4" v-if="avatar" />
            <button @click="$refs.fileInput.click()" class="px-4 py-2 bg-blue-500 text-white rounded">Thay đổi
                avatar</button>
            <input id="avatar" type="file" @change="onFileChange" ref="fileInput" class="hidden" />
        </div>

        <form @submit.prevent="updateProfile" class="w-full max-w-sm">
            <button type="submit" class="w-full px-4 py-2 bg-green-500 text-white rounded">Cập nhật hồ sơ</button>
        </form>

        <router-view />
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    setup() {
        const avatar = ref(null);

        const onFileChange = (e) => {
            let files = e.target.files || e.dataTransfer.files;
            if (!files.length)
                return;
            createImage(files[0]);
        };

        const createImage = (file) => {
            let reader = new FileReader();
            reader.onload = (e) => {
                avatar.value = e.target.result;
            };
            reader.readAsDataURL(file);
        };

        const updateProfile = () => {
            console.log(avatar.value);
        };

        return { avatar, onFileChange, updateProfile };
    }
};
</script>