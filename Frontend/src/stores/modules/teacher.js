import { defineStore } from "pinia";
import teacherService from "../../apis/modules/teacher.js";

export const useTeacherStore = defineStore("teacher", {
  state: () => ({
    tmpCollectionId: null,
    collections: [],
    questionBank: [],
  }),

  actions: {
    async getCollections() {
      try {
        const response = await teacherService.getCollection();
        console.log(response.data);
        this.collections = response.data;
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getQuestionBank(collectionId) {
      try {
        const response = await teacherService.getQuestionBank(collectionId);
        console.log(response.data);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
  },
});
