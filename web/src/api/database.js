/*
 * @Description: 
 * @Author: zhendong.wu
 * @Date: 2021-09-29 09:21:49
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-09-30 10:51:53
 */
import request from '@/utils/request'

export const getTableList = data => {
  return request({
    url: '/api/table/list/',
    method: 'post',
    data,
  })
}

export const createDataField = data => {
  return request({
    url: '/api/table/field/',
    method: 'post',
    data,
  })
}

export const editDataField = data => {
  return request({
    url: '/api/table/field/',
    method: 'put',
    data,
  })
}

export const deleteDataField = data => {
  return request({
    url: '/api/table/field/',
    method: 'delete',
    data,
  })
}

export const getFieldTableList = data => {
  return request({
    url: '/api/table/field/list/',
    method: 'post',
    data,
  })
}

export const getExcel = data => {
  return request({
    url: '/api/table/export/',
    method: 'post',
    data,
  })
}