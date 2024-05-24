<template>
    <div class="p-10 grid grid-cols-3">
        <!-- <div v-if="cheatingDetected" class="bg-red-500 text-white p-4 rounded">
            <p>Bố bắt được mày chuyển tab nha thằng l</p>
        </div> -->
        <div class="left-0">
            <timer />
        </div>

        <div class="flex items-center justify-center min-h-screen">
            <div class="w-full max-w-4xl bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
                <div v-for="(question, index) in questions.student_work" :key="index" class="mb-6">
                    <question-box :question="question" :questionIndex="index" @answer-selected="addAnswer" />
                </div>
                <button @click="submitTest"
                    class="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Nộp bài</button>
            </div>
        </div>
        <div class="menu">
            <menu />
        </div>

    </div>
</template>
<script>
import { ref, reactive, computed, onMounted, onUnmounted } from 'vue';
import { useStudentStore } from '../../../stores/modules/student';
import QuestionBox from '../../../components/test/QuestionBox.vue';
import Timer from '../../../components/test/Timer.vue';
import Menu from '../../../components/test/Menu.vue';

export default {
    components: {
        QuestionBox,
        Timer,
        Menu
    },
    setup() {
        const studentStore = useStudentStore()
        const cheatingDetected = ref(false);
        const group_test_id = ref(null);
        const questions = ref([]);
        const userAnswers = reactive({});
        let student_answer = ref([]);
        const data = computed(() => ({
            group_test_id: group_test_id.value,
            student_answer: student_answer.value
        }));
        const addAnswer = (payload) => {
            const { questionId, answer } = payload;
            console.log(payload)
            student_answer.value[questionId] = answer;
        }
        const handleVisibilityChange = () => {
            if (document.hidden) {
                cheatingDetected.value = true;
            }
        };

        const submitTest = () => {
            console.log(data.value);
        };

        onMounted(async () => {
            group_test_id.value = localStorage.getItem("group_test_id")
            questions.value = await studentStore.getTest(group_test_id.value);
            const length = questions.value.student_work.length;
            student_answer = ref(Array(length).fill().map(() => []));
            document.addEventListener('visibilitychange', handleVisibilityChange);
        });

        onUnmounted(() => {
            document.removeEventListener('visibilitychange', handleVisibilityChange);
        });

        return {
            cheatingDetected,
            questions,
            userAnswers,
            student_answer,
            group_test_id,
            data,
            addAnswer,
            submitTest,
            handleVisibilityChange
        };
    },
};
</script>