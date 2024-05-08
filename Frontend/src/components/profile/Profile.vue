<template>
    <div class="container mx-auto p-4">
        <div class="flex flex-cols-2 space-x-20">
            <div class="avt bg-white shadow-md rounded-md p-6 w-full text-center">
                <img :src="'http://localhost:4444/static/'+ user.avatar_path"
                    class="rounded-full w-64 h-64 text-center">
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