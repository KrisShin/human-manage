/*
 * @Description: 
 * @Author: zhendong.wu
 * @Date: 2021-09-20 22:08:14
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-09-26 00:11:29
 */

import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)

// 引入element-plus
import ElementPlus from 'element-plus'
import './assets/style/element-variables.scss'
// 引入中文语言包
import 'dayjs/locale/zh-cn'
import locale from 'element-plus/lib/locale/lang/zh-cn'
import i18n from './assets/locale'
// 引入路由
import router from './router'

// 引入store
import store from './store'

// 权限控制
import './permission'

// 引入svg图标注册脚本
import 'vite-plugin-svg-icons/register'

// 注册全局组件
import * as Components from './global-components'
Object.entries(Components).forEach(([key, component]) => {
  app.component(key, component)
})

// 错误日志
import useErrorHandler from './error-log'
useErrorHandler(app)

app
  .use(ElementPlus, {
    i18n: i18n.global.t,
  })
  .use(i18n)
  .use(store)
  .use(router)
  .mount('#app')
