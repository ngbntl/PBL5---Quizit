<template>
    <div>
        <div class="sidebar">
            <div class="sidebar-header">
                <h3>Student</h3>
            </div>
            <div class="sidebar-content">
                <router-link to="/student/schedule" class="sidebar-link">Schedule</router-link>
                <router-link to="/student/grades" class="sidebar-link">Grades</router-link>
                <router-link to="/student/attendance" class="sidebar-link">Attendance</router-link>
                <router-link to="/student/assignments" class="sidebar-link">Assignments</router-link>
                <router-link to="/student/notifications" class="sidebar-link">Notifications</router-link>
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>

</style>