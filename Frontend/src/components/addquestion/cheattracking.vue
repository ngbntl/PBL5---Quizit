<template>
    <div>
      <form @submit.prevent="submitAnswers">
        <!-- Your quiz form here -->
        <button type="submit">Submit</button>
      </form>
      <p v-if="cheatingDetected">Cheating detected: same answers submitted twice.</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        submissions: {},
        currentUser: '', // You should set this to the current user
        currentAnswers: [], // You should set this to the current answers
        cheatingDetected: false
      }
    },
    methods: {
      submitAnswers() {
        if (this.submissions[this.currentUser]) {
          if (this.submissions[this.currentUser].toString() === this.currentAnswers.toString()) {
            this.cheatingDetected = true;
          } else {
            this.submissions[this.currentUser] = this.currentAnswers;
            this.cheatingDetected = false;
          }
        } else {
          this.submissions[this.currentUser] = this.currentAnswers;
          this.cheatingDetected = false;
        }
      }
    }
  }
  </script>