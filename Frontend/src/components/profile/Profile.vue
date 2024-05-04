<template>
    <div class="container mx-auto">
        <h1 class="text-2xl font-bold mb-4">Edit Profile</h1>
        <form>
            <div class="mb-4">
                <label for="name" class="block text-gray-700 font-bold mb-2">Name</label>
                <input type="text" id="name" class="border border-gray-300 rounded-md p-2 w-full" v-model="name">
            </div>
            <div class="mb-4">
                <label for="email" class="block text-gray-700 font-bold mb-2">Email</label>
                <input type="email" id="email" class="border border-gray-300 rounded-md p-2 w-full" v-model="email">
            </div>
            <div class="mb-4">
                <label for="bio" class="block text-gray-700 font-bold mb-2">Bio</label>
                <textarea id="bio" class="border border-gray-300 rounded-md p-2 w-full" v-model="bio"></textarea>
            </div>
            <button type="submit"
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Save</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            name: '',
            email: '',
            bio: ''
        }
    }
}
</script>

<style>
/* Add your custom styles here */
</style>