import { createApp } from "vue";
import { createPinia } from "pinia";
import "./style.css";

import "./assets/style.css";
import router from "./router/index.js";

import App from "./App.vue";

const app = createApp(App);
app.use(router);
app.mount("#app");
app.use(createPinia());
