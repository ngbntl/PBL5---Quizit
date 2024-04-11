<template>
    <div class="flex h-screen bg-gray-200">
        <div class="w-64 bg-white p-4 shadow-lg">
            <h2 class="text-3xl m-4 justify-center text-center font-semibold text-blue-500">Quizit</h2>
            <nav>
                <router-link to="/student/schedule"
                    class="block py-2.5 px-4 rounded transition duration-200 hover:bg-blue-500 hover:text-white">Lịch
                    thi</router-link>
                <router-link to="/student/grades"
                    class="block py-2.5 px-4 rounded transition duration-200 hover:bg-blue-500 hover:text-white">Lớp</router-link>
                <router-link to="/student/notifications"
                    class="block py-2.5 px-4 rounded transition duration-200 hover:bg-blue-500 hover:text-white">Thông
                    báo</router-link>
            </nav>
        </div>
        <div class="flex-1 p-10 text-2xl font-bold">
            <router-view />
        </div>
    </div>
</template>

<script>
export default {
    // Your component logic here
}
</script>

<style scoped>
/* Your custom styles here */
</style>