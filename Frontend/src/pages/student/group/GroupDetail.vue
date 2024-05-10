<template>
  <table class="w-full divide-y divide-gray-200">
    <thead class="bg-gray-50">
    <tr>
      <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
        Name
      </th>
      <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
        Age
      </th>
      <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
        Course
      </th>
    </tr>
    </thead>
    <tbody class="bg-white divide-y divide-gray-200">
    <tr v-for="student in students" :key="student.id">
      <td class="px-6 py-4 whitespace-nowrap">
        <div class="text-sm font-medium text-gray-900">{{ student.name }}</div>
      </td>
      <td class="px-6 py-4 whitespace-nowrap">
        <div class="text-sm text-gray-500">{{ student.age }}</div>
      </td>
      <td class="px-6 py-4 whitespace-nowrap">
        <div class="text-sm text-gray-500">{{ student.course }}</div>
      </td>
    </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  data() {
    return {
      students: [
        { id: 1, name: 'John Doe', age: 22, course: 'Computer Science' },
        { id: 2, name: 'Jane Doe', age: 20, course: 'Electrical Engineering' },

      ],
    };
  },
};
</script>