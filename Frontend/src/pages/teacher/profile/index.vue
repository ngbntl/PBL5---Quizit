<template>
    <profile :user="teacher" />
</template>

<script>
import Profile from '../../../components/profile/Profile.vue'
import { useTeacherStore } from '../../../stores/modules/teacher';
import { ref, onMounted } from 'vue';
export default {
    components: {
        Profile
    },
    setup() {
        const teacher = ref({});
        const teacherStore = useTeacherStore();

        onMounted(async () => {
            teacher.value = await teacherStore.getInfor();

        });
        return {
            teacher
        }

    }

}
</script>

<style Profile>

</style>