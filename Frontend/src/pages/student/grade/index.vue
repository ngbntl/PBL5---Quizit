<template>
    <h1 class="text-3xl font-semibold p-4">Các lớp học đã tham gia</h1>
    <div class="flex flex-col">
        <div class=" ">
            <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
                <div class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
                    <table class="min-w-full divide-y divide-gray-200">
                        <thead class="bg-gray-50">
                            <tr>
                                <th scope="col"
                                    class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                    STT
                                </th>
                                <th scope="col"
                                    class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                    Lớp
                                </th>
                                <th scope="col"
                                    class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                    Giáo viên
                                </th>
                                <th scope="col"
                                    class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                                    Ngày tham gia
                                </th>
                            </tr>
                        </thead>
                        <tbody class="bg-white divide-y divide-gray-200  ">
                            <tr v-for="(classItem, index) in classes" :key="index"
                                class="hover:cursor-pointer text-gray-900 hover:text-blue-500">
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <div class="text-sm ">{{ index+1 }}</div>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <div class="text-sm ">{{ classItem.name }}</div>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <div class="text-sm ">{{ classItem.teacher }}</div>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <div class="text-sm ">{{ classItem.date }}</div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    <router-view />
</template>


<script>
export default {
    data() {
        return {
            classes: [
                { name: 'CNPM', teacher: 'Võ Đức Hoàng', date: '2024-02-01' },
                { name: 'QLDA', teacher: 'Nguyễn Thị Minh Hỷ', date: '2024-02-02' },
                // add more classes as needed
            ],
        };
    },
};
</script>

<style>

</style>