# 用户登录

所有账号登录密码都是password
```json
"url": "http://101.34.137.128:9100/api/user/login/",
"method": "POST",
"request": {
    "email": "email",
    "password": "password"
},
"response": {
    "code": 200,
    "data": {
        "create_time": "2021-08-26 15:17:45.963050",
        "department": "财务部",
        "department_id": 1,
        "email": "xueyou.zhang@humanmanage.com",
        "id": 3,
        "name": "张学友",
        "office": "天津",
        "position": "保洁",
        "salary": 8000.0,
        "status": "休假",
        "update_time": "None"
    }
}
```

# 用户列表
获取分页用户列表, page和pageSize可不传, 默认page=1, pageSize=10

```json
"url": "http://101.34.137.128:9100/api/user/list/",
"method": "GET",
"request": {
    "page": 1,
    "pageSize": 3
},
"response": {
    "code": 200,
    "data": [
        {
            "create_time": "2021-08-26 15:13:50.921226",
            "department": "财务部",
            "department_id": 1,
            "email": "dehua.liu@humanmanage.com",
            "id": 1,
            "name": "刘德华",
            "office": "上海",
            "position": "前端开发",
            "salary": 15000.0,
            "status": "在职",
            "update_time": null
        },
        {
            "create_time": "2021-08-26 15:16:43.712553",
            "department": null,
            "department_id": null,
            "email": "dehua.ma@humanmanage.com",
            "id": 2,
            "name": "马德华",
            "office": "成都",
            "position": "Java开发",
            "salary": 18000.0,
            "status": "在职",
            "update_time": null
        },
        {
            "create_time": "2021-08-26 15:17:45.963050",
            "department": "财务部",
            "department_id": 1,
            "email": "xueyou.zhang@humanmanage.com",
            "id": 3,
            "name": "张学友",
            "office": "天津",
            "position": "保洁",
            "salary": 8000.0,
            "status": "休假",
            "update_time": null
        }
    ],
    "page": 1,
    "pageSize": 3,
    "total": 13
}
```

# 菜单列表

获取所有菜单
```json
"url": "http://101.34.137.128:9100/api/menu/list/",
"method": "GET",
"request": null,
"response": {
    "code": 200,
    "data": {
        "业务数据": [
            "其他业务",
            "社内业务",
            "社外业务"
        ],
        "基础数据": [
            "部门信息",
            "公司信息",
            "人员信息"
        ]
    }
}
```


# 增加10条user数据

增加10条user数据
```json
"url": "http://101.34.137.128:9100/api/user/mock/",
"method": "GET",
"request": null,
"response": {
    "code": 200
}
```


# 部门列表

返回所有部门
```json
"url": "http://101.34.137.128:9100/api/department/list/",
"method": "GET",
"request": null,
"response": {
  "code": 200, 
  "data": [
    {
      "id": 1, 
      "name": "保卫部"
    }, 
    {
      "id": 2, 
      "name": "安全部"
    }, 
    {
      "id": 3, 
      "name": "人事部"
    }
  ]
}
```

# 获取单个user信息

获取单个user信息
```json
"url": "http://101.34.137.128:9100/api/user/",
"method": "GET",
"request": null,
"response": {
  "code": 200, 
  "data": {
    "create_time": "2021-08-26 15:17:45.963050", 
    "department": "保洁部", 
    "department_id": 1, 
    "email": "xueyou.zhang@humanmanage.com", 
    "id": 3, 
    "name": "张学有", 
    "office": "内蒙古", 
    "position": "保洁员", 
    "salary": 8000.0, 
    "status": "在职", 
    "update_time": null
  }
}
```

# 新建一个user

新建一个user
```json
"url": "http://101.34.137.128:9100/api/user/",
"method": "POST",
"request": {
    "department_id": 1, 
    "email": "xueyou.zhang@humanmanage.com", 
    "name": "张学有", 
    "office": "内蒙古", 
    "position": "保洁员", 
    "salary": 8000.0, 
    "status": "休假", 
},
"response": {
  "code": 200
}
```


# 编辑一个user

编辑一个user
```json
"url": "http://101.34.137.128:9100/api/user/",
"method": "PUT",
"request": {
    "id":3,
    "department_id": 1, 
    "email": "xueyou.zhang@humanmanage.com", 
    "name": "张学有", 
    "office": "内蒙古", 
    "password": "asdf1234",
    "position": "保洁员", 
    "salary": 8000.0, 
    "status": "休假", 
},
"response": {
  "code": 200
}
```


# 删除一个user

删除一个user
```json
"url": "http://101.34.137.128:9100/api/user/",
"method": "DELETE",
"request": {
    "id":3
},
"response": {
  "code": 200
}
```