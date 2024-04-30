import axios from "axios";

export const baseURL = import.meta.env.VUE_APP_API || "http://localhost:4444";
axios.defaults.headers.common["Authorization"] =
  "Bearer" + localStorage.getItem("token");
export default () => {
  return axios.create({
    baseURL: baseURL,
  });
};
