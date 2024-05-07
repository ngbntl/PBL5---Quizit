import { defineStore } from "pinia";
import teacherService from "../../apis/modules/teacher.js";

export const useTeacherStore = defineStore("teacher", {
  state: () => ({
    tmpCollectionId: null,
    collections: [],
    collectionName: "",
    questionsName: "",
    questionBank: [],
    questions: [],
    bankId: "",
    groupId: "",
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
        //console.log(response.data);
        this.questions = response.data;
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addQuestionBank(bank) {
      try {
        const response = await teacherService.addQuestionBank(bank);
        this.questionBank = this.getQuestionBank(this.tmpCollectionId);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addQuestion(questionBankId, question) {
      try {
        console.log(question);
        const response = await teacherService.addQuestion(
          questionBankId,
          question
        );
        this.questions = this.getQuestions(this.bankId);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getStudents(groupId) {
      try {
        const response = await teacherService.getStudents(groupId);
        console.log(response.data);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getGroups() {
      try {
        const response = await teacherService.getGroups();
        console.log(response.data);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getHiddenGroups() {
      try {
        const response = await teacherService.getHiddenGroups();
        console.log(response.data);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
  },
});
