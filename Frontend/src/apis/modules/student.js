import Api from "../../apis";

export default {
  //group
  getGroups() {
    return Api().get("student/group/?join=1&just_id=0", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },

  joinGroup(group_id) {
    return Api().post(
      `student/group?group_id=${group_id}`,

      {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      }
    );
  },

  //profile
  getInfor() {
    return Api().get("student/", {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      },
    });
  },
};
