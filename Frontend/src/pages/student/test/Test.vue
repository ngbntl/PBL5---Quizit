<template>
    <div class="p-6">
        <h1 class="text-2xl font-bold mb-4">Trang Thi</h1>
        <div v-if="cheatingDetected" class="bg-red-500 text-white p-4 rounded">
            <p>Gian lận đã được phát hiện. Bài thi đã bị dừng.</p>
        </div>
        <div v-else>
            <div v-for="(question, index) in questions" :key="index" class="mb-6">
                <h2 class="text-xl mb-2">{{ question.text }}</h2>
                <div v-for="(answer, index) in question.answers" :key="index" class="mb-2">
                    <input type="radio" :name="'question-' + question.id" :value="answer.id"
                        v-model="userAnswers[question.id]" class="mr-2">
                    <label>{{ answer.text }}</label>
                </div>
            </div>
            <button @click="submitTest" class="bg-blue-500 text-white px-4 py-2 rounded">Nộp bài</button>
        </div>
    </div>
</template>

<script>
import { ref, reactive, onMounted, onUnmounted } from 'vue';

export default {
    setup() {
        const cheatingDetected = ref(false);
        const questions = reactive([
            {
                id: 1,
                text: 'Câu hỏi 1',
                answers: [
                    { id: 'a', text: 'Câu trả lời A' },
                    { id: 'b', text: 'Câu trả lời B' },
                    { id: 'c', text: 'Câu trả lời C' },
                    { id: 'd', text: 'Câu trả lời D' },
                ],
            },
            {
                id: 2,
                text: 'Câu hỏi 2',
                answers: [
                    { id: 'a', text: 'Câu trả lời A' },
                    { id: 'b', text: 'Câu trả lời B' },
                    { id: 'c', text: 'Câu trả lời C' },
                    { id: 'd', text: 'Câu trả lời D' },
                ],
            },

        ]);
        const userAnswers = reactive({});

        const handleVisibilityChange = () => {
            if (document.hidden) {
                cheatingDetected.value = true;
            }
        };

        const submitTest = () => {

        };

        onMounted(() => {
            document.addEventListener('visibilitychange', handleVisibilityChange);
        });

        onUnmounted(() => {
            document.removeEventListener('visibilitychange', handleVisibilityChange);
        });

        return {
            cheatingDetected,
            questions,
            userAnswers,
            submitTest,
        };
    },
};
</script>