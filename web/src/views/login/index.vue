<!--
 * @Description: 
 * @Version: 
 * @Author: zhendong.wu
 * @Date: 2021-08-30 23:22:24
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-08-31 15:53:33
 * @FilePath: /0825/src/views/login/index.vue
-->
<template>
  <div class="login-wrapper">
    <div class="logo">
      <span class="left"></span>
      <span class="right"></span>
    </div>
    <div class="title">
      <p>Welome to IO</p>
      <p>Please Sign-in to your account</p>
    </div>
    <el-form ref="form" :model="formData" hide-required-asterisk :rules="rules">
      <el-form-item prop="email">
        <el-input v-model="formData.email" type="email" placeholder="email"></el-input>
      </el-form-item>
      <el-form-item prop="password">
        <el-input type="password" v-model="formData.password"></el-input>
      </el-form-item>
    </el-form>
    <div style="text-align: right">
      <el-button type="primary" @click="handleLogin">Sign in</el-button>
    </div>
  </div>
</template>

<script>
import { login } from '@/api/user'
import Admin from '@/views/admin/index'
export default {
  name: '',
  props: {

  },
  components: {

  },
  data () {
    return {
      formData: {},
      rules: {
        email: [
          {required: true, message: '请输入email', triggle: 'blur'}
        ],
        password: [
          {required: true, message: '请输入密码', triggle: 'blur'}
        ]
      }
    }
  },
  watch: {
    '$store.state.menuList' (list) {
      // this.getMenuData(list)
    }
  },
  computed: {

  },
  created () {
    this.$store.dispatch('GET_MENULIST')
  },
  mounted () {

  },
  methods: {
    handleLogin () {
      this.$refs.form.validate((valid) => {
        if (valid) {
          const params = {...this.formData}
          login(params)
            .then(res => {
              this.$store.commit('SET_USERINFO', res.data)
              this.$message.success('登录成功')
              this.$router.push({path: '/base/humanInfo'})
            })
        } else {
          return false
        }
      })
    },
    getMenuData (asyncMne) {
      asyncMne.forEach(item => {
        item.children.forEach(ch => {
          let routeItem = {}
          routeItem = ({
            path: ch.path.split('/')[2],
            name: ch.title,
            component: Admin,
            meta: {
              title: ch.title,
              icon: 'menu-circle'
            }
          })

          if (item.title === '基础数据') {
            this.$router.addRoute('Base', routeItem)
          }

          if (item.title === '业务数据') {
            this.$router.addRoute('Data', routeItem)
          }
        })
      })
    },
  }
}
</script>

<style scoped lang="scss">
.login-wrapper {
  position: absolute;
  top: 30vh;
  left: 50%;
  transform: translateX(-50%);
  width: 400px;
  background: #fff;
  padding: 30px;
  border-radius: 10px;
  .title {
    text-align: center;
    font-size: 18px;
    color: #444;
    font-weight: 500;
    line-height: 24px;
  }
  .logo {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    overflow: hidden;
    position: relative;
    margin: 0 150px 15px;
    span {
      width: 100%;
      height: 100%;
      display: inline-block;
      &.left {
        background: #1d2bf1;
        position: absolute;
        left: -50%;
      }
      &.right {
        background: #1bbff3;
      }
    }
  }
}
</style>
