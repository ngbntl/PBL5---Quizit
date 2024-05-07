<template>

    <div>
        <h1>Student List</h1>
        <ul>
            <li v-for="student in teacherStore.students" :key="student.id">
                {{ student.name }}
            </li>
        </ul>
    </div>
</template>

<script>
import { useTeacherStore } from '../../../stores/modules/teacher'
import { onMounted, ref } from 'vue';
export default {
    setup() {
        const teacherStore = useTeacherStore();
        const students = ref([]);
        const id = {
            group_id: teacherStore.groupId
        };
        onMounted(async () => {
            students.value = await teacherStore.getStudents(id.value);
            console.log(id.value)
        });
        return {
            teacherStore,
            students
        };
    }

}
</script>

<style>

    </style>
