import { defineStore } from "pinia";
import teacherService from "../../apis/modules/teacher.js";

export const useTeacherStore = defineStore("teacher", {
  state: () => ({
    tmpCollectionId: null,
    collections: [],
    collectionName: "",
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
    async addCollection(name) {
      try {
        const response = await teacherService.addCollection(name);
        console.log(response.data);
        this.collections = this.getCollections();
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getQuestionBank(collectionId) {
      try {
        const response = await teacherService.getQuestionBank(collectionId);
        console.log(response.data);
        this.questionBank = response.data;
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getQuestions(questionBankId) {
      try {
        const response = await teacherService.getQuestions(questionBankId);
        console.log(response.data);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
  },
});
