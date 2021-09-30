import request from '@/utils/request'

export const getUserList = data => {
  return request({
    url: '/api/user/list/',
    method: 'post',
    data,
  })
}

export const getRole = () => {
  return request({
    url: '/api/user/role/list/',
    method: 'get',
  })
}

export const getQingwu = () => {
  return request({
    url: '/api/user/duty/list/',
    method: 'get',
  })
}

export const getYouxiao = () => {
  return request({
    url: '/api/user/abort/list/',
    method: 'get',
  })
}

export const deleteUser = data => {
  return request({
    url: '/api/user/',
    method: 'delete',
    data,
  })
}

export const getUserInfo = data => {
  return request({
    url: '/api/user/',
    method: 'get',
    params: data,
  })
}

export const addUser = data => {
  return request({
    url: '/api/user/',
    method: 'post',
    headers: { 'Content-Type': 'multipart/form-data' },
    data,
  })
}

export const editUser = data => {
  return request({
    url: '/api/user/',
    method: 'put',
    data,
  })
}

export const getDepartment = data => {
  return request({
    url: '/api/department/list/',
    method: 'get',
    params: data,
  })
}

export const getFactory = () => {
  return request({
    url: '/api/factory/list/',
    method: 'get',
  })
}

export const upload = data => {
  return request({
    url: '/api/upload/',
    method: 'post',
    data,
  })
}
