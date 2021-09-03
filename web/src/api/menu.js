/*
 * @Description: 
 * @Version: 
 * @Author: zhendong.wu
 * @Date: 2021-08-30 11:16:11
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-08-31 09:39:38
 * @FilePath: /0825/src/api/menu.js
 */
import request from './request'

export function getMenuList() {
  return request({
    url: '/menu/list/',
    method: 'get'
  })
}