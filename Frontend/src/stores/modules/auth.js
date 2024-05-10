import { defineStore } from "pinia";
import AuthService from "../../apis/modules/auth.js";
import router from "../../router";
import { useToast } from "vue-toastification";
export const useAuthStore = defineStore("auth", {
  state: () => ({
    role: null,
    isLoggedIn: false,
    token: null,
  }),

  actions: {
    async login(data) {
      try {
        if (data.role === "teacher") {
          const teacher = {
            username: data.username,
            password: data.password,
          };
          const response = await AuthService.loginTeacher(teacher);
          if (response && response.data.access_token) {
            this.token = response.data.access_token;
            localStorage.setItem("token", this.token);
            this.isLoggedIn = true;
            useToast().success("Đăng nhập thành công");
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
            localStorage.setItem("token", this.token);
            this.isLoggedIn = true;
            console.log(response);
            router.push({ name: "student - schedule" });
          }
        }
      } catch (error) {
        if (error.response.data.detail == "Incorrect username or password") {
          useToast().error("Email hoặc mật khẩu không đúng!");
        }
      }
    },
    async signUp(data) {
      try {
        if (data.role === "teacher") {
          const teacher = {
            email: data.email,
            password: data.password,
            name: data.name,
          };
          const response = await AuthService.signUpTeacher(teacher);
          console.log(response);
          useToast().success("Đăng ký thành công");
          router.push({ name: "login" });
        }
        if (data.role === "student") {
          const student = {
            username: data.username,
            password: data.password,
            role: data.role,
          };
          const response = await AuthService.signUpStudent(student);
          console.log(response);
          useToast().success("Đăng ký thành công");
          router.push({ name: "login" });
        }
      } catch (error) {
        if (
          error.response.data.detail ==
          "(2627, b\"Violation of UNIQUE KEY constraint 'unq_tch_ema'. Cannot insert duplicate key in object 'dbo.teacher'. The duplicate key value is (teacher6@gmail.com).DB-Lib error message 20018, severity 14:\\nGeneral SQL Server error: Check messages from the SQL Server\\n\")"
        ) {
          useToast().error("Email đã tồn tại!");
        }
      }
    },
  },
});
