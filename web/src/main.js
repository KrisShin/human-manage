/*
 * @Description: 
 * @Version: 
 * @Author: zhendong.wu
 * @Date: 2021-05-14 09:55:26
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-08-30 09:56:29
 * @FilePath: /0825/src/main.js
 */
import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import './assets/styles/index.scss'
import './assets/icons'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(ElementUI)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
