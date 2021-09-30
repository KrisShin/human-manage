/*
 * @Description: 
 * @Author: zhendong.wu
 * @Date: 2021-09-21 20:44:04
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-09-26 13:44:47
 */
// home.js
const Layout = () => import('@/layout/index.vue')
const Base = () => import('@/views/base/index.vue')

export default [
  {
    path: '/engineering',
    component: Layout,
    name: 'Engineering',
    meta: {
      title: '工程管理',
    },
    icon: 'home',
    children: [
      {
        path: '',
        name: 'EngineeringSearch',
        component: Base,
        meta: {
          title: '工程查询',
          affix: false,
        },
      },
      {
        path: 'gongxu',
        name: 'GongXu',
        component: Base,
        meta: {
          title: '工序查询',
          affix: false,
        },
      },
      {
        path: 'gongwei',
        name: 'GongWei',
        component: Base,
        meta: {
          title: '工位管理',
          affix: false,
        },
      },
    ],
  },
]
