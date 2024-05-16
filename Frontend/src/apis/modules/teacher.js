import Api from "../../apis";

export default {
  //Collection
  getCollection() {
    return Api().get("teacher/collection/", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  addCollection(name) {
    return Api().post("teacher/collection/", name, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },

  //question
  addQuestionBank(bank) {
    return Api().post("teacher/collection/question_bank/", bank, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },

  addQuestion(questionBankId, question) {
    return Api().post(
      `teacher/collection/question_bank/question/?question_bank_id=${questionBankId}`,
      question,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },
  uploadFile(formData, questionId) {
    return Api().post(
      `teacher/collection/question_bank/question/attachment?question_id=${questionId}`,
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },

  getQuestionBank(collectionId) {
    return Api().get(
      `teacher/collection/question_bank/?collection_id=${collectionId}`,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },
  getQuestions(questionBankId) {
    return Api().get(
      `teacher/collection/question_bank/question/?question_bank_id=${questionBankId}`,
      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },

  //groups
  getStudents(groupId) {
    return Api().get(`teacher/group/student?group_id=${groupId}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  getGroups() {
    return Api().get(`teacher/group/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  getHiddenGroups() {
    return Api().get(`teacher/group/?is_show=0`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  addGroup(groupName) {
    return Api().post(`teacher/group/`, groupName, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
  //test
  getTests(group_id) {
    return Api().get(`grouptest/?group_id=${group_id}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },

  //profile
  getInfor() {
    return Api().get(`teacher/`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
};
