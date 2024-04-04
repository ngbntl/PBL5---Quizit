<template>
    <div class="fixed top-0 p-4 flex bg-white">
        <div class="fixed left-12">
            <h1 class="text-5xl font-bold text-blue-600 font-sans">Quizit</h1>
        </div>

        <div class="fixed right-28 space-x-10">
            <router-link to="/" class="text-xl text-gray-500 hover:text-blue-600">Trang chủ</router-link>
            <router-link to="/" class="text-xl text-gray-500 hover:text-blue-600">Liên hệ</router-link>
            <button class="bg-transparent border-1 border-gray-400 p-2 rounded hover:bg-blue-700 hover:text-white">
                <router-link to="/login" class="text-xl text-gray-500 hover:text-white">Đăng nhập</router-link>
            </button>
            <button class="bg-blue-500 text-white text-xl px-4 py-2 rounded hover:bg-blue-700">
                <router-link to="/register" class="text-xl">Đăng ký</router-link>
            </button>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>
</style>