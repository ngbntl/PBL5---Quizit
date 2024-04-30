const teacher = [
  {
    path: "/teacher",
    name: "teacher",
    component: () => import("../layouts/teacherLayout.vue"),
    children: [
      {
        path: "schedule",
        name: "teacher-schedule",
        component: () => import("../pages/teacher/schedule/index.vue"),
      },
      {
        path: "group",
        name: "teacher-group",
        component: () => import("../pages/teacher/group/index.vue"),
      },

      {
        path: "quizes",
        name: "teacher-quizes",
        component: () => import("../pages/teacher/quizzes/index.vue"),
      },
      {
        path: "profile",
        name: "teacher-profile",
        component: () => import("../pages/teacher/profile/index.vue"),
      },
    ],
  },
];
export default teacher;
