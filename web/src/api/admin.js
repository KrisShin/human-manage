/*
 * @Description: 
 * @Version: 
 * @Author: zhendong.wu
 * @Date: 2021-08-29 23:24:37
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-08-31 20:09:45
 * @FilePath: /0825/src/api/admin.js
 */
import request from './request'

export function getUserList(data) {
  return request({
    url: '/user/list/',
    method: 'post',
    data: data
  })
}

export function userInfo(data, method) {
  const params = {
    url: '/user/',
    method: method
  }
  if (method === 'get') {
    params.params = data
  } else {
    params.data = data
  }
  return request(params)
}

export function getDepartment() {
  return request({
    url: 'department/list/',
    method: 'get'
  })
}