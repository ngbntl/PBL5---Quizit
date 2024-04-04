const auth = [
  {
    path: "/",
    component: () => import("../layouts/authLayout.vue"),
    children: [
      {
        path: "/login",
        name: "login",
        component: () => import("../pages/auth/LoginPage.vue"),
        meta: {
          title: "Login",
          requiresAuth: false,
        },
      },
    ],
  },
];
export default auth;
