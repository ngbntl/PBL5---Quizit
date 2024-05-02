<template>
    <div class="editor h-1/2 w-2/3 items-center justify-center ml-1/2">
        <div v-for="(question, index) in questions" :key="index">
            <h1 class="text-2xl p-3">Câu {{ index + 1 }}</h1>
            <p>Câu hỏi</p>
            <QuillEditor :content="question.content" />
        </div>
    </div>
</template>

<script>
import { onMounted, ref } from 'vue';
import { useRouter } from 'vue-router';
import QuillEditor from '../../../components/quill/QuillEditor.vue';
import { useTeacherStore } from '../../../stores/modules/teacher.js';

export default {
    components: {
        QuillEditor,
    },
    setup() {
        const teacherStore = useTeacherStore();
        const questions = ref([]);
        const route = useRouter();

        onMounted(async () => {
            const id = route.currentRoute.value.params.id;
            console.log(id);
            questions.value = await teacherStore.getQuestions(id);
            console.log(questions.value);
        });

        return {
            questions,
        };
    },
};
</script>