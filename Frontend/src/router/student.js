const student = [
  {
    path: "/student",
    name: "student",
    component: () => import("../pages/student/index.vue"),
    children: [
      {
        path: "schedule",
        name: "student - schedule",
        component: () => import("../pages/student/schedule/index.vue"),
      },
    ],
  },
];
export default student;
