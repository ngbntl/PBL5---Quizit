import { defineStore } from "pinia";
import AuthService from "../../apis/modules/auth.js";
import router from "../../router";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    role: null,
    isLoggedIn: false,
    token: null, // corrected here
  }),

  actions: {
    async login(data) {
      try {
        if (data.role === "teacher") {
          const teacher = {
            username: data.username,
            password: data.password,
          };
          console.log(teacher);
          const response = await AuthService.loginTeacher(teacher);
          if (response && response.data.access_token) {
            this.token = response.data.access_token;
            this.isLoggedIn = true;
            console.log(response);
            router.push({ name: "teacher-schedule" });
          }
        }
        if (data.role === "student") {
          const student = {
            username: data.username,
            password: data.password,
          };
          const response = await AuthService.loginStudent(student);
          if (response && response.data.access_token) {
            this.token = response.data.access_token;
            this.isLoggedIn = true;
            console.log(response);
            router.push({ name: "student - schedule" });
          }
        }
      } catch (error) {
        console.error(error);
      }
    },
  },
});
