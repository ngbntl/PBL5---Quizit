<template>
    <div class="flex justify-center space-x-2 mb-4">
        <div v-for="index in totalQuestions" :key="index" @click="goToQuestion(index)"
            class="cursor-pointer border rounded-full w-8 h-8 flex items-center justify-center hover:bg-gray-100">{{
            index }}</div>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    props: {
        totalQuestions: Number // Số lượng câu hỏi
    },
    setup(props) {
        const goToQuestion = (index) => {
            // Code chuyển đến câu hỏi ở vị trí index
        }

        return {
            totalQuestions: ref(props.totalQuestions),
            goToQuestion
        }
    }
}
</script>