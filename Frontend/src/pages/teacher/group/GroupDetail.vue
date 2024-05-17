<template>
    <div class="ml-8">
        <div class="flex items-center ">
            <button @click="$router.go(-1)" class="ml-10 mt-5">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                    stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                </svg>
            </button>
            <h1 class="text-2xl ml-10 mt-5"> vcc </h1>
        </div>
        <div>
            <div class="flex items-center">
                <DownOutlined v-if="showRequests" @click="toggleRequests" class="ml-4 mt-4" />
                <RightOutlined v-else @click="toggleRequests" class="ml-4 mt-4" />
                <h1 class="text-xl ml-8 mt-6">Yêu cầu tham gia</h1>
            </div>
            <div class="student" v-for="request in requests" :key="request.id" v-show="showRequests">
                <Card :student="request" />

                <div class="absolute right-16 top-1/4 mt-8 space-x-5"><button @click="acceptRequest(request.id)"
                        class="bg-green-500 hover:bg-green-700 text-white font-bold py-3 px-3 rounded-full">
                        <fa icon="fa-check" class="rounded-full" />
                    </button>
                    <button @click="deleteRequest(request.id)"
                        class="bg-red-500 hover:bg-red-700 text-white font-bold py-3 px-4 rounded-full">
                        <fa icon="fa-x" class="rounded-full" />

                    </button>
                </div>
            </div>

        </div>
        <div>
            <div class="flex items-center">
                <DownOutlined v-if="showStudents" class="ml-4 mt-4 hover:cursor-pointer" @click="toggleStudents" />
                <RightOutlined v-else class="ml-4 mt-4  hover:cursor-pointer" @click="toggleStudents" />
                <h1 class="text-xl ml-8 mt-6 hover:cursor-pointer" @click="toggleStudents">Danh sách sinh viên</h1>
                <div class="absolute right-10 mt-4" v-show="showStudents">
                    <add-student />
                </div>
            </div>
            <div class="student" v-for="student in students" :key="student.id" v-show="showStudents">
                <Card :student="student" />
            </div>

        </div>
        <div>
            <div class="flex items-center">
                <DownOutlined v-if="showTests" @click="toggleTests" class="ml-4 mt-4" />
                <RightOutlined v-else @click="toggleTests" class="ml-4 mt-4" />
                <h1 class="text-xl ml-8 mt-6">Bài kiểm tra</h1>
                <add-test />
            </div>
            <div class="student" v-for="test in tests" :key="test.id" v-show="showTests">
                <TestCard :test="test" />
            </div>

        </div>
    </div>

</template>

<script>
import { useTeacherStore } from '../../../stores/modules/teacher'
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import Card from '../../../components/profile/Card.vue';
import { DownOutlined, RightOutlined } from "@ant-design/icons-vue";
import AddStudent from '../../../components/modal/AddStudent.vue';
import TestCard from '../../../components/questionBank/TestCard.vue';
import AddTest from '../../../components/modal/AddTest.vue';

export default {
    components: { Card, DownOutlined, RightOutlined, TestCard, AddStudent, AddTest },

    setup() {
        const teacherStore = useTeacherStore();
        const students = ref([]);
        const route = useRoute();
        const groupId = route.params.id;
        const showStudents = ref(true);
        const showRequests = ref(true);
        const showTests = ref(true);
        const tests = ref([]);
        const requests = ref([]);

        const toggleTests = () => {
            showTests.value = !showTests.value;
        }
        const toggleRequests = () => {
            showRequests.value = !showRequests.value;
        }
        const toggleStudents = () => {
            showStudents.value = !showStudents.value;
        }

        onMounted(async () => {
            students.value = await teacherStore.getStudents(groupId);
            tests.value = await teacherStore.getTests(groupId);
            requests.value = await teacherStore.getRequests(groupId);
            console.log(tests.value)
        });

        return {
            teacherStore,
            students,
            groupId,
            showStudents,
            showRequests,
            showTests,
            tests,
            requests,

            toggleTests,
            toggleRequests,
            toggleStudents
        };
    }
}
</script>

<style>

</style>