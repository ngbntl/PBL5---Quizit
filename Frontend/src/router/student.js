const student = [
  {
    path: "/student",
    name: "student",
    component: () => import("../layouts/studentLayout.vue"),
    children: [
      {
        path: "schedule",
        name: "student - schedule",
        component: () => import("../pages/student/schedule/index.vue"),
      },
      {
        path: "group",
        name: "student - group",
        component: () => import("../pages/student/group/index.vue"),
      },
      {
        path: "group/:id",
        name: "student-group-detail",
        component: () => import("../pages/student/group/GroupDetail.vue"),
      },
      {
        path: "notif",
        name: "student - notif",
        component: () => import("../pages/student/notif/index.vue"),
      },
      {
        path: "profile",
        name: "student - profile",
        component: () => import("../pages/student/profile/index.vue"),
      },
      // {
      //   path: "profile/edit",
      //   name: "student - profile - edit",
      //   component: () => import("../pages/student/profile/Edit.vue"),
      // },
      // {
      //   path: "profile/change-password",
      //   name: "student - profile - change-password",
      //   component: () => import("../pages/student/profile/ChangePassword.vue"),
      // },
    ],
  },
];
export default student;
