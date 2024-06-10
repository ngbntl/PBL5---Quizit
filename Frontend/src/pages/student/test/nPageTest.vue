<template>
    <div class="p-10">
        <timer :minutes="duration" class="fixed" @time-up="submitTest" />

        <div class="flex items-center justify-center min-h-screen">
            <div class="w-full max-w-4xl bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
                <div v-for="(question, index) in paginatedQuestions" :key="index" class="mb-6"
                    :id="`question-${index+1}`">
                    <question-box :question="question" :questionIndex="index"
                        @answer-selected="addAnswer($event, index)" />
                </div>
                <div class="text-right ">
                    <a-button @click="showConfirm" class="bg-blue-500 text-white rounded-md">Nộp bài</a-button>
                </div>
                <div class="pagination space-x-3">
                    <a-button @click="prevPage" :disabled="currentPage === 1">Trước</a-button>
                    <span class=" space-x-3">Trang {{ currentPage }} trên {{ totalPages }}</span>
                    <a-button @click="nextPage" :disabled="currentPage === totalPages">Tiếp theo</a-button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, reactive, computed, onMounted, onUnmounted } from 'vue';
import { useStudentStore } from '../../../stores/modules/student';
import QuestionBox from '../../../components/test/QuestionBox.vue';
import Timer from '../../../components/test/Timer.vue';


import { Modal } from 'ant-design-vue';
import { h } from 'vue';
import { ExclamationCircleOutlined } from '@ant-design/icons-vue';
import { useRouter } from 'vue-router';
import { useWebSocketStore } from '../../../stores/modules/webSocket';
import { eventType } from 'ant-design-vue/es/_util/type';
import { useToast } from 'vue-toastification';
export default {
    components: {
        QuestionBox,
        Timer
    },
    setup() {
        const studentStore = useStudentStore();
        const questions = ref([]);
        const currentPage = ref(1);
        const questionsPerPage = ref(5);
        const duration = ref(null);
        const tabSwitchCount = ref(0);
        const totalPages = computed(() => Math.ceil(questions.value.length / questionsPerPage.value));



        const paginatedQuestions = computed(() => {
            const startIndex = (currentPage.value - 1) * questionsPerPage.value;
            return questions.value.slice(startIndex, startIndex + questionsPerPage.value);
        });

        onMounted(async () => {
            let test = await localStorage.getItem('test');
            duration.value = localStorage.getItem("duration");
            const parsedTest = JSON.parse(test);
            questions.value = parsedTest.student_work;
        });

        const nextPage = () => {
            if (currentPage.value < totalPages.value) {
                currentPage.value++;
            }
        };

        const prevPage = () => {
            if (currentPage.value > 1) {
                currentPage.value--;
            }
        };

        //  không nhấn chuột phải
        const contextMenuHandler = (event) => {
            event.preventDefault();

        };

        onMounted(() => {
            window.addEventListener('contextmenu', contextMenuHandler);
        });

        onUnmounted(() => {
            window.removeEventListener('contextmenu', contextMenuHandler);
        });

        // popup cảnh báo khi đóng cửa sổ
        onMounted(() => {
            window.addEventListener('beforeunload', handleBeforeUnload);
        });

        onUnmounted(() => {
            window.removeEventListener('beforeunload', handleBeforeUnload);
        });

        const handleBeforeUnload = (event) => {
            event.preventDefault();
            event.returnValue = '';
        };
        //chặn phím
        window.addEventListener('keydown', function (e) {
            if (e.key === 'F5' || e.key === 'Ctrl' || e.key === 'Tab' || e.key === 'Alt') {
                e.preventDefault();
            }
        });


        // đếm số lần chuyển tab
        const handleVisibilityChange = () => {
            let tabSwitchLim = localStorage.getItem('tolerance')
            if (tabSwitchLim > 0) {
                if (document.visibilityState === 'hidden') {
                    tabSwitchCount.value++;
                    if (tabSwitchCount.value > tabSwitchLim) {
                        submitTest();

                    } else {
                        Modal.warning({
                            title: 'phát hiện hành vi gian lận!',
                            content: h('div', { style: 'color:red;' },
                                `Bạn đã chuyển tab ${tabSwitchCount.value} lần. Nếu chuyển tab quá ${tabSwitchLim} lần, bài kiểm tra sẽ tự động nộp.`,),
                        });
                    }
                }
            }
        };

        document.addEventListener('visibilitychange', handleVisibilityChange);
        onUnmounted(() => {
            document.removeEventListener('visibilitychange', handleVisibilityChange);
        });






        const addAnswer = (answer, index) => {
            console.log({
                detail: {
                    index: index,
                    answer: [answer]
                }
            });
        }
        const submitTest = () => {


        }

        const showConfirm = () => {
            Modal.confirm({
                title: 'Bạn chắc chắn nộp bài?',
                icon: h(ExclamationCircleOutlined),
                content: h(
                    'div',
                    {
                        style: 'color:red;',
                    },
                    '',
                ),
                onOk() {

                    submitTest();
                    //  router.push('/point');
                },
                onCancel() {
                    console.log('Hủy');
                },
                class: 'test',
            });
        };

        return {
            questions,
            currentPage,
            totalPages,
            paginatedQuestions,
            duration,
            tabSwitchCount,
            handleVisibilityChange,
            showConfirm,


            nextPage,
            prevPage,
            addAnswer
        };
    }
};
</script>