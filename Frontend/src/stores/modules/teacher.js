import { defineStore } from "pinia";
import teacherService from "../../apis/modules/teacher.js";
import { useToast } from "vue-toastification";

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
    questionId: "",
  }),

  actions: {
    //collection

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

    //question

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
        this.questionBank = await this.getQuestionBank(this.tmpCollectionId);
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
        useToast().success("Đã thêm câu hỏi");

        this.questions = await this.getQuestions(this.bankId);

        return response.data;
      } catch (error) {
        console.error(error);
        useToast().error("Thêm thất bại");
      }
    },
    async uploadFile(formData, questionId) {
      try {
        const response = await teacherService.uploadFile(formData, questionId);
        this.questions = await this.getQuestions(this.bankId);

        return response.data;
      } catch (error) {
        console.error(error);
        useToast().error("Tải ảnh lên thất bại!");
      }
    },

    //students

    async getStudents(groupId) {
      try {
        const response = await teacherService.getStudents(groupId);
        // console.log(response.data);
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
    async addGroup(groupName) {
      try {
        const response = await teacherService.addGroup(groupName);
        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async getInfor() {
      try {
        const response = await teacherService.getInfor();

        return response.data;
      } catch (error) {
        console.error(error);
      }
    },
  },
});
