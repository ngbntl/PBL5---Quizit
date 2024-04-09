<template>

    <div class="regis grid grid-cols-2 m-10 h-full">
        <Header />
        <div class="img w-2/3 bg-white m-28 shadow-md">
            <img src="/src/assets/img/register.png" alt="" />
        </div>
        <div class="form my-28 mx-12 bg-white shadow-md p-12 w-2/3">
            <h2 class="text-3xl font-bold text-center my-14">Đăng ký tài khoản</h2>
            <div class="mb-4">
                <input type="email" v-model="email" :class="`w-full px-3 py-2 border rounded-md focus:outline-none ${
            emailError
              ? 'border-red-500'
              : 'border-gray-300 focus:border-blue-500'
          }`" placeholder="Họ" />
            </div>
            <div class="mb-4">
                <input type="email" v-model="email" :class="`w-full px-3 py-2 border rounded-md focus:outline-none ${
            emailError
              ? 'border-red-500'
              : 'border-gray-300 focus:border-blue-500'
          }`" placeholder="Tên" />
            </div>
            <div class="mb-4">
                <input type="email" v-model="email" :class="`w-full px-3 py-2 border rounded-md focus:outline-none ${
            emailError
              ? 'border-red-500'
              : 'border-gray-300 focus:border-blue-500'
          }`" placeholder="Email" />
            </div>
            <div class="mb-4">
                <select name="role" id=""
                    class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500 text-gray-500">
                    <option value="student">Học sinh</option>
                    <option value="teacher">Giáo viên</option>
                </select>
            </div>

            <div class="mb-4">
                <input type="password" v-model="password"
                    class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500"
                    placeholder="Mật khẩu" />


                <button class="absolute right-4 top-4 focus:outline-none" @click="togglePasswordVisibility">
                    <svg v-if="showPassword" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-400"
                        fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M15 12a3 3 0 11-6 0 3 3 0 016 0zm-3 8a9 9 0 01-9-9m9 9a9 9 0 009-9m-9 9h9m-9-9a9 9 0 019-9m-9 9a9 9 0 00-9 9h9z" />
                    </svg>

                </button>
            </div>

            <button @click="validateForm"
                class="w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-500 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
                Đăng ký
            </button>
            <p class="mt-4 text-center">
                Đã có tài khoản?
                <a href="/login" class="text-blue-500 hover:text-blue-700">Đăng Nhập</a>
            </p>
        </div>
    </div>
    <router-view />
</template>

<script>
import Header from "../../components/Header.vue";

export default {
    components: { Header },
};
</script>

<style></style>
