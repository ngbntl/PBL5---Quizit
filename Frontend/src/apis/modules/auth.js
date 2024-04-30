import Api from "../../apis";

export default {
  login(data) {
    return Api().post("Login", {
      email: data.email,
      password: data.password,
    });
  },
};
