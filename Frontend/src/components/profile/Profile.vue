<template>
    <div class="container mx-auto p-4">
        <div class="flex flex-cols-2 space-x-20">
            <div class="avt bg-white shadow-md rounded-md p-6 w-full text-center">
                <div class="flex-row">
                    <img :src="'http://localhost:4444/static/'+ user.avatar_path"
                        class="rounded-full w-64 h-64 text-center">

                    <label for="file-upload"
                        class="rounded-md px-8 py-2 border-2 fixed left-1/4 -ml-10 border-transparent bg-blue-500 focus:outline-none text-white placeholder-gray-400 transition-all duration-300 shadow-md">
                        Chọn ảnh
                    </label>
                    <input id="file-upload" type="file" @change="handleFileChange" class="hidden mb-4" multiple />

                    <img :src="imagePreview" alt="Uploaded Image" v-if="imagePreview" class="mt-4 w-32 h-32" />
                </div>
                <h1 class="text-2xl font-bold text-center">{{ user.name }}</h1>
                <p class="text-gray-500 text-center">{{ user.email }}</p>
            </div>

        </div>
    </div>
</template>

<script>
export default {
    props: {
        user: Object
    },

}
</script>

<style scoped>
</style>