<template>
    <div class="flex h-screen">
        <div class="text-4xl font-bold text-center">
            Thời gian còn lại: {{ minutes }}:{{ seconds < 10 ? '0' + seconds : seconds }} </div>
        </div>
</template>
<script>
import { ref, onMounted, watch } from 'vue';
export default {
    name: 'CountdownTimer',
    props: {
        minutes: {
            type: Number,
            required: true
        }
    },
    setup(props, { emit }) {
        const totalSeconds = ref(localStorage.getItem('remainingTime') || props.minutes * 60);
        const minutes = ref(Math.floor(totalSeconds.value / 60));
        const seconds = ref(totalSeconds.value % 60);
        const updateCountdown = () => {
            if (totalSeconds.value > 0) {
                totalSeconds.value--;
                localStorage.setItem('remainingTime', totalSeconds.value);
                minutes.value = Math.floor(totalSeconds.value / 60);
                seconds.value = totalSeconds.value % 60;
            } else {
                emit('time-up');
            }
        };
        onMounted(() => {
            const interval = setInterval(updateCountdown, 1000);
            return () => clearInterval(interval);
        });
        watch(() => props.minutes, (newVal, oldVal) => {
            totalSeconds.value = newVal * 60;
            minutes.value = newVal;
            seconds.value = 0;
        });
        return {
            minutes,
            seconds
        };
    },
};
</script>
<style>
  /* Add Tailwind CSS classes here for styling */
</style>