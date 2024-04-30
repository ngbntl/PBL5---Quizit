import Api from "../../apis";

export default {
  loginTeacher(data) {
    const params = new URLSearchParams();
    params.append("username", data.username);
    params.append("password", data.password);
    return Api().post("auth/token?role=teacher", params, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });
  },

  loginStudent(data) {
    const params = new URLSearchParams();
    params.append("username", data.username);
    params.append("password", data.password);
    return Api().post("auth/token?role=student", params, {
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });
  },
};
