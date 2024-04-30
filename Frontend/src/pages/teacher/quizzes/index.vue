<template>

    <div class="flex flex-wrap">
        <Collection v-for="(item, index) in collections" :key="index" />
    </div>
    <router-view />
</template>

<script>
import Collection from '../../../components/collection/Collection.vue';
export default {
    components: {
        Collection,
    },
    data() {
        return {
            collections: [1, 2, 3, 4, 5]
        }
    }
}
</script>

<style>

</style>