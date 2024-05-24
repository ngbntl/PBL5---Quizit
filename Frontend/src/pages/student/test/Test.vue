<template>
    <div class="p-10 ">
        <!-- <div v-if="cheatingDetected" class="bg-red-500 text-white p-4 rounded">
            <p>Bố bắt được mày chuyển tab nha thằng l</p>
        </div> -->

        <timer :minutes="duration" class="fixed" @time-up="submitTest" />


        <div class="flex items-center justify-center min-h-screen">
            <div class="w-full max-w-4xl bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
                <div v-for="(question, index) in questions.student_work" :key="index" class="mb-6"
                    :id="`question-${index+1}`">
                    <question-box :question="question" :questionIndex="index" @answer-selected="addAnswer" />
                </div>
                <a-button @click="showConfirm">Nộp bài</a-button>
            </div>


            <div class="fixed right-0 top-10">
                <Menu :totalQuestions="length" :answeredQuestions="answeredQuestions"
                    :selectedQuestion="selectedQuestion" @go-to-question="goToQuestion"
                    class="fixed right-0 top-1/2 mr-20" />
            </div>
        </div>
    </div>

</template>
<script>
import { ref, reactive, computed, onMounted, onUnmounted } from 'vue';
import { useStudentStore } from '../../../stores/modules/student';
import QuestionBox from '../../../components/test/QuestionBox.vue';
import Timer from '../../../components/test/Timer.vue';
import Menu from '../../../components/test/Menu.vue';
import { Modal } from 'ant-design-vue';
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
        const duration = ref(null);
        duration.value = localStorage.getItem("duration");
        const selectedQuestion = ref(null);





        const data = computed(() => ({
            group_test_id: group_test_id.value,
            student_answer: student_answer.value
        }));
        const answeredQuestions = ref([]); // Mảng để theo dõi các câu hỏi đã được trả lời

        const addAnswer = (payload) => {
            const { questionId, answer } = payload;
            student_answer.value[questionId] = answer;
            selectedQuestion.value = questionId;
            answeredQuestions.value.push(questionId); // Thêm câu hỏi vào mảng câu hỏi đã trả lời
        }

        const handleVisibilityChange = () => {
            if (document.hidden) {
                cheatingDetected.value = true;
            }
        };

        const submitTest = () => {
            console.log(data.value);
        };
        const length = ref(null)
        onMounted(async () => {
            group_test_id.value = localStorage.getItem("group_test_id")
            questions.value = await studentStore.getTest(group_test_id.value);
            length.value = questions.value.student_work.length;
            student_answer = ref(Array(length).fill().map(() => []));
            console.log(duration.value)
            document.addEventListener('visibilitychange', handleVisibilityChange);
        });

        onUnmounted(() => {
            document.removeEventListener('visibilitychange', handleVisibilityChange);
        });
        const goToQuestion = (index) => {
            const questionElement = document.getElementById(`question-${index}`);
            if (questionElement) {
                questionElement.scrollIntoView({ behavior: 'smooth' });
            }
        };

        const showConfirm = () => {
            modal.confirm({
                title: 'Do you Want to delete these items?',
                icon: h(ExclamationCircleOutlined),
                content: h(
                    'div',
                    {
                        style: 'color:red;',
                    },
                    'Some descriptions',
                ),
                onOk() {
                    console.log('OK');
                },
                onCancel() {
                    console.log('Cancel');
                },
                class: 'test',
            });
        };

        return {
            cheatingDetected,
            questions,
            userAnswers,
            student_answer,
            group_test_id,
            data,
            duration,
            length,
            selectedQuestion,
            answeredQuestions,

            goToQuestion,
            showConfirm,
            addAnswer,
            submitTest,
            handleVisibilityChange
        };
    },
};
</script>