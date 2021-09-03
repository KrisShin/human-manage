/*
 * @Description: 
 * @Version: 
 * @Author: zhendong.wu
 * @Date: 2021-08-29 23:15:44
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-08-31 09:26:06
 * @FilePath: /0825/src/api/user.js
 */
import request from './request'

export function login(data) {
  return request({
    url: '/user/login/',
    method: 'post',
    data
  })
}

