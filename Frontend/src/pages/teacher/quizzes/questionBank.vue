<template>
    <h1 class="text-2xl ml-10 mt-5">Bộ sưu tập: {{ collectionName }}</h1>
    <div class="flex justify-end m-4 -mt-4 mr-8">
        <add-question-bank />
    </div>
    <div class="flex flex-wrap">
        <Bank v-for="(item, index) in banks" :key="index" :collection="item" @click="getName(item.name)" />
    </div>

    <router-view />
</template>

<script>
import { defineComponent, ref, onMounted, watch } from 'vue';
import { useTeacherStore } from '../../../stores/modules/teacher.js';
import { useRoute } from 'vue-router';
import Bank from '../../../components/questionBank/Bank.vue';
import Addform from '../../../components/modal/Addform.vue';
import AddQuestionBank from '../../../components/modal/AddQuestionBank.vue';
export default defineComponent({
    components: {
        Bank,
        Addform,
        AddQuestionBank
    },

    setup() {
        const banks = ref([]);
        const teacherStore = useTeacherStore();
        const route = useRoute();
        const collectionName = teacherStore.collectionName;
        onMounted(async () => {
            const id = route.params.id;
            banks.value = await teacherStore.getQuestionBank(id);
            console.log(banks.value);
        });
        const getName = (name) => {
            teacherStore.questionsName = name;
        };
        watch(() => teacherStore.questionBank, (newQuestionBank) => {
            banks.value = newQuestionBank;
        });
        return {
            banks,
            collectionName,
            getName,
        };
    }
})
</script>

<style>

</style>