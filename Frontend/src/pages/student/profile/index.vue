<template>
  <div class="bg-white shadow rounded-lg p-6">
    <div class="flex items-center space-x-4">
      <img class="h-16 w-16 rounded-full" :src="student.image" alt="Student Image">
      <div>
        <h2 class="text-xl font-medium text-gray-800">{{ student.name }}</h2>
        <p class="text-gray-600">{{ student.course }}</p>
      </div>
    </div>
    <div class="mt-6">
      <h3 class="text-lg font-medium text-gray-800">About</h3>
      <p class="text-gray-600">{{ student.about }}</p>
    </div>
    <div class="mt-6">
      <h3 class="text-lg font-medium text-gray-800">Contact Information</h3>
      <div class="grid grid-cols-2 gap-4 mt-2">
        <div>
          <p class="text-gray-600">Email:</p>
          <p class="text-gray-800">{{ student.email }}</p>
        </div>
        <div>
          <p class="text-gray-600">Phone:</p>
          <p class="text-gray-800">{{ student.phone }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    student: {
      type: Object,
      required: true,
    },
  },
};
</script>