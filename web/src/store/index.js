/*
 * @Description: 
 * @Version: 
 * @Author: zhendong.wu
 * @Date: 2021-05-14 09:55:26
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-09-01 10:29:17
 * @FilePath: /0825/src/store/index.js
 */
import Vue from 'vue'
import Vuex from 'vuex'
import { getMenuList } from '../api/menu'
import persistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    menuList: [],
    userinfo: null,
    sidebarHidden: false,
    historyLink: []
  },
  mutations: {
    SET_MENU_LIST (state, data) {
      state.menuList = data
    },
    SET_USERINFO (state, data) {
      state.userinfo = data
    },
    SET_SIDEBAR_IS_HIDDEN (state, data) {
      state.sidebarHidden = data
    },
    SET_HISTORY_LINK (state, data) {
      state.historyLink.push(data)
    },
    DEL_HISTORY_LINK (state, index) {
      state.historyLink.splice(index, 1)
    }
  },
  actions: {
    GET_MENULIST ({commit}) {
      getMenuList()
        .then(res => {
          commit('SET_MENU_LIST', res.data)
        })
    },

    GET_AND_SET_HISTORY_LINK ({state, commit}, data) {
      const history = [...state.historyLink]
      const route = JSON.parse(data)
      const hasNewLink = history.some(item => {
        return item.path === route.path
      })
      if (!hasNewLink) {
        commit('SET_HISTORY_LINK', route)
      }
    },

    DEL_HISTORY_LINK ({state, commit}, data) {
      const history = [...state.historyLink]
      const route = JSON.parse(data)
      let idx = -1
      history.forEach((item, index) => {
        if (item.path === data.path) {
          idx = index
        }
      })
      commit('DEL_HISTORY_LINK', idx)  
    }
  },
  modules: {
  },
  plugins: [
    persistedState()
  ]
})
