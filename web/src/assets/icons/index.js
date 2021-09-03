/*
 * @Description:
 * @Version:
 * @Author: zhendong.wu
 * @Date: 2021-07-02 16:50:24
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-08-25 13:55:10
 * @FilePath: /0825/src/assets/icons/index.js
 */
import Vue from 'vue'
import SvgIcon from '@components/SvgIcon'// svg component

// register globally
Vue.component('svg-icon', SvgIcon)

const req = require.context('./svg', false, /\.svg$/)
const requireAll = requireContext => requireContext.keys().map(requireContext)
requireAll(req)
