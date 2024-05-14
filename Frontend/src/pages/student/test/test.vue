<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Trang Trắc Nghiệm với Vue 3</title>
  <script src="https://unpkg.com/vue@next"></script>
</head>
<body>
<div id="app">
  <h1>Trắc nghiệm Vue 3</h1>
  <div v-if="!showResult">
    <div v-for="(question, index) in questions" :key="index">
      <p>{{ question.question }}</p>
      <ul>
        <li v-for="(option, optionIndex) in question.options" :key="optionIndex" @click="selectAnswer(index, optionIndex)">{{ option }}</li>
      </ul>
    </div>
    <button @click="showResults()">Xem Kết Quả</button>
  </div>
  <div v-if="showResult">
    <h2>Kết quả</h2>
    <p>Số câu đúng: {{ correctAnswers }}</p>
  </div>
</div>
<script>
  const app = Vue.createApp({
    data() {
      return {
        questions: [
          {
            question: 'Câu hỏi số 1?',
            options: ['Đáp án 1', 'Đáp án 2', 'Đáp án 3', 'Đáp án 4'],
            correctAnswer: 1
          },
          {
            question: 'Câu hỏi số 2?',
            options: ['Đáp án 1', 'Đáp án 2', 'Đáp án 3', 'Đáp án 4'],
            correctAnswer: 0
          }
        ],
        userAnswers: [],
        showResult: false
      };
    },
    computed: {
      correctAnswers() {
        return this.questions.filter((question, index) => question.correctAnswer === this.userAnswers[index]).length;
      }
    },
    methods: {
      selectAnswer(questionIndex, optionIndex) {
        this.userAnswers[questionIndex] = optionIndex;
      },
      showResults() {
        this.showResult = true;
      }
    }
  });
  app.mount('#app');
</script>
</body>
</html>
