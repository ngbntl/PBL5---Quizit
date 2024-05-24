<template>
    <div>
        <a-button type="primary" @click="showModal">Tạo bài kiểm tra</a-button>
        <a-modal v-model:open="open" title="Tạo bải kiểm tra" @ok="handleOk">
            <template #footer>
                <a-button key="back" @click="handleCancel">Hủy</a-button>
                <a-button key="submit" type="primary" :loading="loading" @click="handleOk">Xác nhận</a-button>
            </template>

            <div class="flex items-center p-4">
                <label class="w-1/3 mb-2">Tên bài kiểm tra: </label>
                <input type="text" v-model="name"
                    class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                    placeholder="Nhập tên bài kiểm tra" />
            </div>
            <!-- <div class="flex items-center p-4">
                <label class="w-1/3 mb-2">Chọn bộ sưu tập: </label>
                <select name="" id=""
                    class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                    v-model="selectedCollection">
                    <option v-for="collection in collections" :key="collection.id" :value="collection.id">
                        {{ collection.name }}
                    </option>
                </select>
            </div> -->


            <div v-for="(struct, idx) in structure" :key="idx" class="p-4">
                <label class="block mb-2">Chọn ngân hàng câu hỏi: </label>
                <select name="" id=""
                    class="w-2/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                    v-model="struct.question_bank_id">
                    <option v-for="questionBank in questionBanks" :key="questionBank.id" :value="questionBank.id">
                        {{ questionBank.name }}
                    </option>
                </select>
                <button @click="removeStructureRow(idx)" class="bg-red-500 text-white px-4 py-2 rounded mt-4 ml-4">
                    Xóa
                </button>



                <div v-for="(num, numindex) in struct.number_of_question" :key="numindex" class="p-4">
                    <div class="flex justify-between mb-2 items-center">
                        <div class="w-1/3  flex items-center">
                            <label class="w-1/2 mb-2">Độ khó: </label>
                            <select name="" id=""
                                class="w-1/2 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                                v-model.number="num.difficulty">
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                                <option value="4">4</option>
                                <option value="5">5</option>

                            </select>
                        </div>
                        <div class="w-2/3 pl-2 flex items-center">
                            <label class="w-2/3 mb-2">Số lượng câu hỏi: </label>
                            <input type="number" v-model="num.number_of_question"
                                class="w-1/3 px-3 py-2 text-gray-700 border rounded-lg focus:outline-none focus:shadow-outline"
                                placeholder="Nhập số lượng câu hỏi" />
                        </div>
                        <button @click="removeSNumberQuestion(numindex)"
                            class="w-1/5 bg-red-500 text-white px-4 py-2 rounded ml-4">
                            Xóa
                        </button>
                    </div>
                </div>

                <button @click="addSNumberQuestion(struct)" class="bg-blue-500 text-white px-4 py-2 rounded mt-4">
                    Thêm Câu hỏi
                </button>

            </div>
            <button @click="addStructureRow" class="bg-blue-500 text-white px-4 py-2 rounded mt-4">
                Thêm ngân hàng câu hỏi
            </button>






        </a-modal>
    </div>
</template>

<script>
import { ref, watch, computed } from "vue";
import { useTeacherStore } from "../../stores/modules/teacher";
import Vue3TagsInput from "vue3-tags-input";
import router from '../../router';
import { useRouter } from 'vue-router';
export default {
    components: { Vue3TagsInput },
    setup() {
        const teacherStore = useTeacherStore();
        const loading = ref(false);
        const open = ref(false);
        const collections = ref('');
        const selectedCollection = ref(null);
        const name = ref('');
        const router = useRouter()
        const structure = ref([
            {
                question_bank_id: null,
                number_of_question: [
                    {
                        difficulty: null,
                        number_of_question: null
                    }
                ]
            }
        ]);
        const test = computed(() => ({
            collection_id: collections.value,
            name: name.value,
            structure: structure.value
        }));

        // watch(selectedCollection, async (newCollectionId) => {
        //     if (newCollectionId) {
        //         questionBanks.value = await teacherStore.getQuestionBank(
        //             newCollectionId
        //         );
        //         test.value.collection_id = newCollectionId;

        //     }
        // });
        watch(name, (newName) => {
            test.value.name = newName;
        });




        const questionBanks = ref([])

        const addQuestionBankRow = () => {
            questionBankIds.value.push({});
        };
        const removeQuestionBankRow = (index) => {
            questionBankIds.value.splice(index, 1);
        };
        const addStructureRow = () => {
            structure.value.push({
                question_bank_id: null,
                number: [],
                number_of_question: []
            });
        }
        const removeStructureRow = (index) => {
            structure.value.splice(index, 1);
        }

        const addSNumberQuestion = (struct) => {
            struct.number_of_question.push({
                difficulty: null,
                number_of_question: null
            });
        }
        const removeSNumberQuestion = (struct, numindex) => {
            struct.number_of_question.splice(numindex, 1);
        }
        const showModal = async () => {
            open.value = true;
            collections.value = router.currentRoute.value.params.id;
            teacherStore.tmpCollectionId = collections.value;

            questionBanks.value = await teacherStore.getQuestionBank(
                collections.value
            );
            console.log(collections.value)
        };

        const handleOk = async () => {
            loading.value = true;
            console.log(test.value)

            teacherStore.addTest(test.value);
            setTimeout(() => {
                loading.value = false;
                open.value = false;
            }, 2000);
        };

        const handleCancel = () => {
            open.value = false;
        };

        return {
            open,
            loading,
            collections,
            selectedCollection,
            test,
            questionBanks,
            structure,
            name,

            addStructureRow,
            removeStructureRow,
            addQuestionBankRow,
            removeQuestionBankRow,
            addSNumberQuestion,
            removeSNumberQuestion,
            showModal,
            handleOk,
            handleCancel,
        };
    },
};
</script>
