/*
 * @Description: 
 * @Version: 
 * @Author: zhendong.wu
 * @Date: 2021-05-14 09:55:26
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-08-31 15:53:10
 * @FilePath: /0825/src/router/index.js
 */
import Vue from 'vue'
import VueRouter from 'vue-router'
import Layout from '@components/Layout/index'
import store from '../store/index'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: Layout,
    redirect: '/base/humanInfo',
    hidden: true
  },
  {
    path: '/base',
    component: Layout,
    name: 'Base',
    redirect: '/base/humanInfo',
    meta: {
      title: '基础数据',
      icon: 'menu-edit'
    },
    children: [
      {
        path: 'humanInfo',
        component: () => import('@/views/admin/index'),
        name: 'HumanInfo',
        meta: {
          title: '人员信息',
          icon: 'menu-circle'
        }
      },
      {
        path: 'companyInfo',
        component: () => import('@/views/admin/index'),
        name: 'companyInfo',
        meta: {
          title: '公司信息',
          icon: 'menu-circle'
        }
      },
      {
        path: 'departmentInfo',
        component: () => import('@/views/admin/index'),
        name: 'departmentInfo',
        meta: {
          title: '部门信息',
          icon: 'menu-circle'
        }
      }
    ]
  },
  {
    path: '/data',
    component: Layout,
    name: 'Data',
    redirect: '/data/other',
    meta: {
      title: '业务数据',
      icon: 'menu-edit'
    },
    children: [
      {
        path: 'other',
        component: () => import('@/views/admin/index'),
        name: 'HumanInfo',
        meta: {
          title: '其他业务',
          icon: 'menu-circle'
        }
      },
      {
        path: 'Internal',
        component: () => import('@/views/admin/index'),
        name: 'companyInfo',
        meta: {
          title: '社内业务',
          icon: 'menu-circle'
        }
      },
      {
        path: 'external',
        component: () => import('@/views/admin/index'),
        name: 'departmentInfo',
        meta: {
          title: '社外业务',
          icon: 'menu-circle'
        }
      }
    ]
  },
  {
    path: '/login',
    name: 'Login',
    hidden: true,
    component: () => import('@/views/login/index')
  },
  { path: '*', redirect: '/404', hidden: true }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  if (!store.state.userinfo && to.path !== '/login') {
    next({ name: 'Login' })
  } else {
    next()
  }
}) 

export default router
