<template>
    <div class="flex flex-wrap">
        <div v-for="card in cards" :key="card.id"
            class="m-4 w-60 h-72 bg-slate-100 rounded-3xl text-gray-500 p-4 flex flex-col items-start justify-center gap-3 hover:bg-gray-400 hover:shadow-2xl hover:shadow-sky-400 hover:text-white hover:cursor-pointer transition-shadow">
            <div class="w-52 h-40 bg-gray-300 rounded-2xl"></div>
            <div class="">
                <p class="font-extrabold">{{ card.name }}</p>
                <p class="">{{ card.description }}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        cards: {
            type: Array,
            required: true
        }
    }
}
</script>

<style>

</style>