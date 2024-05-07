import Api from "../../apis";

export default {
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
  getStudents(groupId) {
    return Api().get(`teacher/group/student`, groupId, {
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
};
