// home.js
const Layout = () => import('@/layout/index.vue')
const Base = () => import('@/views/base/index.vue')
const BaseData = () => import('@/views/basedata/index.vue')
export default [
  {
    path: '/project',
    component: Layout,
    name: 'Project',
    meta: {
      title: '项目维护',
    },
    icon: 'home',
    children: [
      {
        path: '',
        name: 'Data',
        component: BaseData,
        meta: {
          title: '数据库维护',
          affix: true,
        },
      },
      {
        path: 'guojihua',
        name: 'Guojihua',
        component: Base,
        meta: {
          title: '国际化语言对照表',
          affix: true,
        },
      },
      {
        path: 'message',
        name: 'Message',
        component: Base,
        meta: {
          title: 'message信息维护',
          affix: true,
        },
      },
      {
        path: 'kuangjia',
        name: 'Kuangjia',
        component: Base,
        meta: {
          title: '框架配置',
          affix: true,
        },
      },
    ],
  },
]
