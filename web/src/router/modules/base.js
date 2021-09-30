// home.js
const Layout = () => import('@/layout/index.vue')
const Base = () => import('@/views/base/index.vue')
const UserDetail = () => import('@/views/base/addOrEdit.vue')

export default [
  {
    path: '/base',
    component: Layout,
    name: 'Base',
    meta: {
      title: '基础数据维护',
    },
    icon: 'home',
    children: [
      {
        path: '',
        name: 'User',
        component: Base,
        meta: {
          title: '用户管理',
          affix: false,
          t: 'UserManagement'
        },
      },
      {
        path: 'userdetail/:isEdit/:userId',
        name: 'UserDetail',
        component: UserDetail,
        meta: {
          title: '编辑',
          affix: false,
        },
        hidden: true,
      },
      {
        path: 'gongchang',
        name: 'Gongchang',
        component: Base,
        meta: {
          title: '工厂管理',
          affix: false,
        },
      },
      {
        path: 'department',
        name: 'Department',
        component: Base,
        meta: {
          title: '部门管理',
          affix: false,
          t: 'DepartmentManagement'
        },
      },
    ],
  },
]
