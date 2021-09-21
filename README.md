# 准备工作

1. 安装python3.6及以上版本
2. 安装nodejs10及以上版本
3. 安装postgresql11及以上版本

# 配置服务环境

### python Flask环境配置

1. 安装虚拟环境pipenv

    ```bash
    pip3 install pipenv
    ```

2. 安装虚拟环境, 配置虚拟环境, 请确认项目目录下有Pipfile

    ```bash
    cd human-manage-server
    pipenv install
    ```

### PostgreSql 配置

1. 进入postgresql, 创建user

    ```sql
    create user humanuser with password 'humanuser';
    ```

2. 创建database

    ```sql
    create database humanmanage with owner 'humanuser';
    ```

3. 退出postgresql, 导入表结构和数据

    ```bash
    psql -U humanuser -d humanmanage < data.sql
    ```

### 启动后台服务

1. 代码配置数据库端口

    ```bash
    修改config/db_config.py
    第11行改为你自己的postgresql的接口, 默认为5432
    port = '5432'
    保存并退出
    ```

2. 激活虚拟环境

    ```bash
    pipenv shell
    ```

3. 启动flask服务

    ```bash
    python manage.py
    ```

### 启动前端服务

1. 进入human-manage-web

    ```bash
    cd human-manage-web
    ```

2. 配置运行环境

    ```bash
    npm i
    ```

3. 修改服务接口, 打开.env.development

    ```bash
    修改第三行为:
    VUE_APP_BASE_URL_API = 'http://localhost:9100'
    ```

4. 启动前端服务

    ```bash
    npm run serve
    ```

### 查看页面

打开浏览器进入 localhost:8082
