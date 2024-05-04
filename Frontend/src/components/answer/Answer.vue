<template>
    <div>
        <div v-if="multipleCorrectAnswers">
            <div v-for="(answer, index) in answers" :key="index" class="flex items-center">
                <input type="checkbox" :checked="answer.is_correct" :disabled="true" class="mr-2">
                <label>{{ answer.content }}</label>
            </div>
        </div>
        <div v-else>
            <div v-for="(answer, index) in answers" :key="index" class="flex items-center">
                <input type="radio" :checked="answer.is_correct" :disabled="true" class="mr-2">
                <label>{{ answer.content }}</label>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        answers: {
            type: Array,
            required: true
        }
    },
    computed: {
        multipleCorrectAnswers() {
            return this.answers.filter(answer => answer.is_correct).length > 1;
        }
    }
}
</script>

<style>
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';
</style>