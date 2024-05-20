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
                <DownOutlined v-if="showStudents" @click="toggleStudents" class="ml-4 mt-4" />
                <RightOutlined v-else @click="toggleStudents" class="ml-4 mt-4" />
                <h1 class="text-xl ml-8 mt-6">Danh sách sinh viên</h1>
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

            </div>
            <div class="flex flex-wrap justify-between" v-show="showTests">
                <TestCard class="m-2 max-w-xs" :test="test" v-for="test in tests" :key="test.id" />
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
import TestCard from '../../../components/questionBank/TestCard.vue';

export default {
    components: { Card, DownOutlined, RightOutlined, TestCard },
    setup() {
        const teacherStore = useTeacherStore();
        const students = ref([]);
        const route = useRoute();
        const groupId = route.params.id;
        const showStudents = ref(true);
        const showRequests = ref(true);
        const showTests = ref(true);
        const tests = ref([]);


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
            tests.value = await teacherStore.getGroupTests(groupId);
        });

        return {
            teacherStore,
            students,
            groupId,
            showStudents,
            showRequests,
            showTests,
            tests,

            toggleTests,
            toggleRequests,
            toggleStudents
        };
    }
}
</script>

<style>

</style>