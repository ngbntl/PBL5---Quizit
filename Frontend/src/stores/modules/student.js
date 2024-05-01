import { defineStore } from "pinia";
import studentService from "../../apis/modules/student.js";

export const useStudentStore = defineStore("student", {
  state: () => ({}),

  actions: {
    async getGroups() {
      try {
        const response = await studentService.getGroups();
        console.log(response.data);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
  },
});
