<template>
    <div class="bg-gray-200 p-4 text-center rounded-lg mb-4">
        <p>{{ timeLeft }}</p>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';

export default {
    setup() {
        const timeLeft = ref(60); // Thời gian đếm ngược, ví dụ 60 giây

        onMounted(() => {
            const interval = setInterval(() => {
                if (timeLeft.value > 0) {
                    timeLeft.value--;
                } else {
                    // Trigger event hoặc hành động khi hết thời gian
                    clearInterval(interval);
                }
            }, 1000);
        });

        return {
            timeLeft
        }
    }
}
</script>