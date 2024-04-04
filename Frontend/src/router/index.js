import { createRouter, createWebHistory } from "vue-router";
import auth from "./auth.js";

const routes = [...auth];

const router = createRouter({
  history: createWebHistory(),

  routes,
});

export default router;
