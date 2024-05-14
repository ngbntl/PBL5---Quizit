<template>
  <div class="flex items-center">
    <button @click="$router.go(-1)" class="ml-10 mt-5">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
           stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
      </svg>
    </button>
    <h1 class="text-2xl ml-10 mt-5"> vcc </h1>
  </div>
  <div>

    <div class="student" v-for="student in students" :key="student.id">
      <Card :student="student" />
    </div>

  </div>
</template>

<script>
import { useTeacherStore } from '../../../stores/modules/teacher'
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';
import Card from '../../../components/profile/Card.vue';
export default {
  components: { Card },
  setup() {
    const teacherStore = useTeacherStore();
    const students = ref([]);
    const route = useRoute();
    const groupId = route.params.id;
    console.log(groupId)
    onMounted(async () => {
      students.value = await teacherStore.getStudents(groupId);
      console.log(students.value)
    });
    return {

      teacherStore,
      students,
      groupId
    };
  }

}
</script>

<style>

</style>
