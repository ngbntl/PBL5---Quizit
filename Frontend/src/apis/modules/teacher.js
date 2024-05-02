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
};
