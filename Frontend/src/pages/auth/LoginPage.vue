<template>
    <div class="w-screen">
        <Header class="fixed z-50 bg-white" />
        <h1 class="mt-24 mx-24 text-4xl font-bold">Đăng nhập để bắt đầu</h1>
        <div class="grid grid-cols-2 gap-4 m-10 mt-20 ml-24 h-full w-full">
            <div class="img w-2/3 ml-24 rounded-md shadow-lg">
                <img src="/src/assets/img/Exams-bro.png" alt="" />
            </div>

            <div class="p-6 bg-white rounded shadow-md w-1/2">
                <h2 class="text-3xl font-bold text-center my-16">Đăng nhập</h2>

                <div class="mb-4">

                    <div class="mt-2 flex flex-wrap space-x-6">
                        <div>
                            <label class="inline-flex items-center">
                                <input type="radio" class="form-radio text-blue-600 h-4 w-4" name="role" value="teacher"
                                    v-model="role">
                                <span class="ml-2 text-gray-700">Giáo viên</span>
                            </label>
                        </div>
                        <div>
                            <label class="inline-flex items-center">
                                <input type="radio" class="form-radio text-blue-600 h-4 w-4" name="role" value="student"
                                    v-model="role">
                                <span class="ml-2 text-gray-700">Học Sinh</span>
                            </label>
                        </div>
                    </div>
                </div>


                <div class="mb-4">


                    <input type="email" v-model="email" @blur="validateEmail" :class="`w-full px-3 py-2 border rounded-md focus:outline-none ${
              emailError
                ? 'border-red-500'
                : 'border-gray-300 focus:border-blue-500'
            }`" placeholder="Email" />
                    <p v-if="emailError" class="text-red-500 text-sm p-1">
                        {{ emailError }}
                    </p>
                </div>
                <div class="mb-4">
                    <input type="password" v-model="password" @blur="validatePassword" :class="`w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500focus:outline-none ${
              passwordError
                ? 'border-red-500'
                : 'border-gray-300 focus:border-blue-500'
            }`" placeholder="Mật khẩu" />
                    <p v-if="passwordError" class="text-red-500 text-sm p-1">
                        {{ passwordError }}
                    </p>
                    <button class="absolute right-4 top-4 focus:outline-none" @click="togglePasswordVisibility">
                        <svg v-if="showPassword" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-400"
                            fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M15 12a3 3 0 11-6 0 3 3 0 016 0zm-3 8a9 9 0 01-9-9m9 9a9 9 0 009-9m-9 9h9m-9-9a9 9 0 019-9m-9 9a9 9 0 00-9 9h9z" />
                        </svg>
                        <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-400" fill="none"
                            viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M15 12a3 3 0 11-6 0 3 3 0 016 0zm-3 8a9 9 0 01-9-9m9 9a9 9 0 009-9m-9 9h9m-9-9a9 9 0 019-9m-9 9a9 9 0 00-9 9h9z" />
                        </svg>
                    </button>
                </div>
                <p class="text-right text-blue-500 hover:text-blue-700 cursor-pointer pb-2">
                    Quên mật khẩu?
                </p>
                <button @click="validateForm"
                    class="w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-500 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                    Đăng nhập
                </button>
                <p class="mt-4 text-center">
                    Bạn chưa có tài khoản?
                    <a href="/register" class="text-blue-500 hover:text-blue-700">Đăng ký</a>
                </p>
            </div>
        </div>
    </div>
    <router-view />
</template>

<script>
import { ref } from 'vue';
import Header from "../../components/header/Header.vue";
import { useAuthStore } from "../../stores/modules/auth.js";
export default {
    components: { Header },
    setup() {
        const email = ref("");
        const password = ref("");
        const emailError = ref("");
        const passwordError = ref("");
        const role = ref("Teacher");

        const validateEmail = () => {
            if (email.value === "") {
                emailError.value = "Vui lòng nhập email.";
            } else if (!/\S+@\S+\.\S+/.test(email.value)) {
                emailError.value = "Định dạng email không hợp lệ.";
            } else {
                emailError.value = "";
            }
        };

        const validatePassword = () => {
            if (password.value === "") {
                passwordError.value = "Vui lòng nhập mật khẩu.";
            } else if (password.value.length < 6) {
                passwordError.value = "Mật khẩu phải có ít nhất 6 ký tự.";
            } else {
                passwordError.value = "";
            }
        };

        const validateForm = () => {
            validateEmail();
            validatePassword();
            if (emailError.value || passwordError.value) {
                return;
            }
            submitForm();

        };

        const submitForm = () => {
            const data = {
                username: email.value,
                password: password.value,
                role: role.value
            };
            const authStore = useAuthStore();

            authStore.login(data);

        };

        return {
            role,
            email,
            password,
            emailError,
            passwordError,
            validateEmail,
            validatePassword,
            validateForm,
            submitForm
        };
    },
};
</script>

<style>
.w-screen {
  overflow-x: hidden;
}
</style>
