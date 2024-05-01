import Api from "../../apis";

export default {
  getCollection() {
    return Api().get("teacher/collection/", {
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
};
