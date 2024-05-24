<template>
    <div class="p-4 bg-white shadow rounded-lg mb-4">
        <h2>Câu: {{ questionIndex +1 }}</h2>
        <h2 class="text-lg font-semibold mb-2">{{ question.content }}</h2>

        <div v-if="question.attachment">
            <img v-for="(img, index) in question.attachment" :key="index" :src="'http://localhost:4444/static/'+ img"
                class="p-10 w-1/2" />
        </div>
        <ul>
            <li v-for="(choice, index) in question.answer.text" :key="index"
                class="p-2 cursor-pointer border rounded-lg hover:bg-gray-100" @click="selectAnswer(index, $event)">
                <input v-if="question.answer.correct.length > 1" type="checkbox" :value="choice"
                    v-model="userAnswers[question.id]" @click.stop>
                <input v-else type="radio" :value="choice" v-model="userAnswers[question.id]" @click.stop>
                {{ choice }}
            </li>
        </ul>
    </div>
</template>
<script>
import { ref } from 'vue';
import StudentLayout from '../../layouts/studentLayout.vue';

export default {
    props: {
        question: Object,
        questionIndex: Number,
    },
    setup(props, { emit }) {
        const userAnswers = ref({});
        const studentAnswers = ref([]);
        const selectAnswer = (index, event) => {
            const inputElement = event.target.querySelector('input');
            if (inputElement) {
                inputElement.click();
            }
            if (!studentAnswers.value[props.questionIndex]) {
                studentAnswers.value[props.questionIndex] = [];
            }
            if (inputElement.type === 'checkbox') {
                const answerIndex = studentAnswers.value[props.questionIndex].indexOf(index);
                if (answerIndex > -1) {
                    studentAnswers.value[props.questionIndex].splice(answerIndex, 1);
                } else {
                    studentAnswers.value[props.questionIndex].push(index);
                }
            } else {
                studentAnswers.value[props.questionIndex] = [index];
            }
            emit('answer-selected', { questionId: props.questionIndex, answer: studentAnswers.value[props.questionIndex] });
        }

        return {
            question: ref(props.question),
            userAnswers,
            studentAnswers,
            selectAnswer
        }
    }
}
</script>