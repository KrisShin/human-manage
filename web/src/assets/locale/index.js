/*
 * @Description: 
 * @Author: zhendong.wu
 * @Date: 2021-09-24 11:36:21
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-09-25 23:52:15
 */
import en from './en'
import zh from './zh'
import ja from './ja'
import store from '@/store'
import {createI18n} from 'vue-i18n'
import enLocale from 'element-plus/lib/locale/lang/en'
import zhLocale from 'element-plus/lib/locale/lang/zh-cn'
import jaLocale from 'element-plus/lib/locale/lang/ja'

const messages = {
  en: {
    ...en,
    ...enLocale,
  },
  zh: {
    ...zh,
    ...zhLocale,
  },
  ja: {
    ...ja,
    ...jaLocale,
  },
}

function getLanguage() {
  return store.getters['language'] || 'zh'
}

const i18n = new createI18n({
  fallbackLocale: 'zh',
  legacy: false,
  locale: getLanguage(),
  messages,
})

export default i18n
