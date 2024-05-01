import Api from "../../apis";

export default {
  getGroups() {
    return Api().get("student/group/?join=1&just_id=0", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
};
