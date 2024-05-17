<template>
    <div class="flex items-center">
        <button @click="$router.go(-1)" class="ml-10 mt-5">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
        </button>
        <h1 class="text-2xl ml-10 mt-5">Bộ sưu tập: {{ collectionName }}</h1>

    </div>




    <div class="flex flex-wrap group hover:cursor-pointer hover:text-blue-500" @click="toggleQuestionBanks">
        <DownOutlined v-if="showQuestionBanks" class="ml-4 mt-6" />
        <RightOutlined v-else class="ml-4 mt-6" />
        <h1 class="text-xl p-4">Ngân hàng câu hỏi</h1>
        <div class="absolute right-10 m-4 mr-8" v-show="showQuestionBanks">
            <add-question-bank />
        </div>
    </div>
    <div class="flex flex-wrap" v-show="showQuestionBanks">
        <Bank v-for="(item, index) in banks" :key="index" :collection="item" @click="getName(item.name)" />
    </div>


    <div class="flex flex-wrap group hover:cursor-pointer hover:text-blue-500" @click="toggleTests">
        <DownOutlined v-if="showTests" class="ml-4 mt-6" />
        <RightOutlined v-else class="ml-4 mt-6" />
        <h1 class="text-xl p-4">Đề thi</h1>
    </div>

    <router-view />
</template>

<script>
import { defineComponent, ref, onMounted, watch } from 'vue';
import { useTeacherStore } from '../../../stores/modules/teacher.js';
import { useRoute } from 'vue-router';
import Bank from '../../../components/questionBank/Bank.vue';
import Addform from '../../../components/modal/Addform.vue';
import { DownOutlined, RightOutlined } from "@ant-design/icons-vue";

import AddQuestionBank from '../../../components/modal/AddQuestionBank.vue';
export default defineComponent({
    components: {
        Bank,
        Addform,
        AddQuestionBank,
        DownOutlined,
        RightOutlined
    },

    setup() {
        const banks = ref([]);
        const teacherStore = useTeacherStore();
        const route = useRoute();
        const collectionName = teacherStore.collectionName;
        const showQuestionBanks = ref(false);
        const showTests = ref(false);

        const toggleQuestionBanks = () => {
            showQuestionBanks.value = !showQuestionBanks.value;
        };
        const toggleTests = () => {
            showTests.value = !showTests.value;
        };

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
            showQuestionBanks,
            showTests,
            toggleTests,
            toggleQuestionBanks,
            getName,
        };
    }
})
</script>

<style>

</style>