<template>
    <div>
        <a-button type="primary" @click="showModal">Thêm câu hỏi</a-button>
        <a-modal v-model:open="open" title="Thêm câu hỏi" @ok="handleOk" :width="800">
            <template #footer>
                <a-button key="back" @click="handleCancel">Hủy</a-button>
                <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Xác nhận</a-button>
            </template>
            <div class="p-4">
                <label class="block mb-2 font-bold">Câu hỏi: </label>
                <!-- <input v-model="content"
                    class="input rounded-md px-8 py-2  border-2 border-transparent focus:outline-none focus:border-blue-500 placeholder-gray-400 transition-all duration-300 shadow-md"
                    placeholder="Nhập câu hỏi..." required="" type="text" />
                
                -->
                <Editor @add-question="handleContentUpdate" :response="response" />

                <label class="block mb-2 mt-4 font-bold">Độ khó: </label>
                <select v-model="difficulty"
                    class="input rounded-md px-8 py-2  border-2 border-transparent focus:outline-none focus:border-blue-500 placeholder-gray-400 transition-all duration-300 shadow-md">
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                </select>
                <label class="block mb-2 mt-4 font-bold">Đáp án: </label>
                <div v-for="(answer, index) in answers" :key="index">
                    <input type="checkbox" v-model="answers[index].isCorrect" />
                    <input v-model="answers[index].text"
                        class="input rounded-md m-2 px-8 py-2  border-2 border-transparent focus:outline-none focus:border-blue-500 placeholder-gray-400 transition-all duration-300 shadow-md"
                        placeholder="Nhập đáp án..." required="" type="text" />

                    <a-button type="primary" class="bg-red-500" @click="removeAnswer(index)">Xóa</a-button>

                </div>
                <a-button type="primary" @click="addAnswer" class="mt-4">Thêm đáp án</a-button>
            </div>
        </a-modal>
    </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useTeacherStore } from '../../stores/modules/teacher';
import { useRoute } from 'vue-router';
import Editor from '../quill/Editor.vue';

export default {
    components: {
        Editor

    },
    setup() {
        const teacherStore = useTeacherStore();
        const loading = ref(false);
        const open = ref(false);
        const route = useRoute();
        const content = ref(null);
        const difficulty = ref(1);
        const answers = ref([{ text: '', isCorrect: false }]);
        const collection = computed(() => ({ question: question.value, answers: answers.value }));


        const handleContentUpdate = (textFromEditor) => {
            content.value = textFromEditor.replace(/<\/?p>/g, '');

        }



        const showModal = () => {
            open.value = true;
        };
        const id = route.params.id;

        const handleOk = async () => {

            loading.value = true;
            const question = {
                content: content.value,
                answer: answers.value
                    .map(answer => answer.isCorrect ? { content: answer.text, is_correct: answer.isCorrect } : { content: answer.text }),
                difficulty: difficulty.value
            };

            const questions = [question];
            const response = await teacherStore.addQuestion(id, questions);

            console.log(response.toString());
            setTimeout(() => {
                loading.value = false;
                open.value = false;
            }, 1000);
        };



        const handleCancel = () => {
            open.value = false;
        };

        const addAnswer = () => {
            answers.value.push({ text: '', isCorrect: false });
        };
        const removeAnswer = (index) => {
            answers.value.splice(index, 1);
        }

        return {
            open,
            loading,

            answers,
            content,
            difficulty,
            handleContentUpdate,

            addAnswer,
            removeAnswer,
            collection,
            showModal,
            handleOk,
            handleCancel,
            addAnswer
        };
    }
}
</script>
<style scoped>

</style>