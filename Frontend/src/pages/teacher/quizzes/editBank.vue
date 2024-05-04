<template>
    <h1 class="text-2xl ml-10 mt-5">Bộ câu hỏi: {{ questionsName }} </h1>
    <add-question class="flex justify-end mx-8 " />

    <div class="editor relative h-1/2 w-3/4 items-center justify-center left-28">
        <div v-for="(question, index) in questions" :key="index" class=" mb-10 rounded-lg m-4 ml-8 shadow-md">
            <h1 class="text-2xl p-3 ml-4">Câu {{ index + 1 }}</h1>
            <p class="ml-4 font-bold">
                Câu hỏi: </p>
            <p class="ml-4 p-4">
                {{ question.content }}
            </p>

            <p class="ml-4 font-bold">
                Đáp án: </p>
            <answer :answers="question.answer" class="p-4" />
        </div>
    </div>
</template>

<script>
import { onMounted, ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import QuillEditor from '../../../components/quill/QuillEditor.vue';
import { useTeacherStore } from '../../../stores/modules/teacher.js';
import AddQuestion from '../../../components/addquestion/Addquestion.vue';

import Answer from '../../../components/answer/Answer.vue';

export default {
    components: {
        QuillEditor,
        Answer,
        AddQuestion,
    },
    setup() {
        const teacherStore = useTeacherStore();
        const questions = ref([]);
        const showAddQuestion = ref(false);
        const route = useRouter();
        const questionsName = teacherStore.questionsName;

        const addQuestion = (newQuestion) => {
            questions.value.push(newQuestion);
            showAddQuestion.value = false;
        };

        onMounted(async () => {
            const id = route.currentRoute.value.params.id;
            teacherStore.bankId = id;
            console.log(id);
            questions.value = await teacherStore.getQuestions(id);

            // console.log(questions.value);
        });
        watch(() => teacherStore.questions, (newQuestion) => {
            questions.value = newQuestion;
        });

        return {
            questions,
            questionsName,
            showAddQuestion,
            addQuestion,
        };
    },
};
</script>