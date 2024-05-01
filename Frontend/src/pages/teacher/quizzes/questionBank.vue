<template>

    <div class="flex flex-wrap">
        <Collection v-for="(item, index) in banks" :key="index" />
    </div>

    <router-view />
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue';
import Collection from '../../../components/collection/Collection.vue';
import { useTeacherStore } from '../../../stores/modules/teacher.js';

export default defineComponent({
    components: {
        Collection,
    },

    setup() {
        const collections = ref([]);
        const teacherStore = useTeacherStore();

        onMounted(async () => {
            console.log("ccc");
            collections.value = await teacherStore.getQuestionBank(teacherStore.tmpCollectionId);
        });

        return {
            collections
        };
    }
})
</script>

<style>

</style>