<!--
 * @Descripttion: 
 * @version: 
 * @Date: 2021-04-20 11:06:21
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-09-26 11:03:45
 * @Author: huzhushan@126.com
 * @HomePage: https://huzhushan.gitee.io/vue3-element-admin
 * @Github: https://github.com/huzhushan/vue3-element-admin
 * @Donate: https://huzhushan.gitee.io/vue3-element-admin/donate/
-->
<template>
  <div class="login">
    <el-form class="form" :model="model" :rules="rules" ref="loginForm">
      <h1 class="title">7ERP Admin</h1>
      <el-form-item prop="user_cd">
        <el-input
          class="text"
          v-model="model.user_cd"
          prefix-icon="el-icon-user-solid"
          clearable
          :placeholder="t('I18n.UserPw')"
        />
      </el-form-item>
      <el-form-item prop="password">
        <el-input
          class="text"
          v-model="model.password"
          prefix-icon="el-icon-lock"
          show-password
          clearable
          placeholder="密码"
        />
      </el-form-item>
      <el-form-item>
        <el-button
          :loading="loading"
          type="primary"
          class="btn"
          @click="submit"
        >
          {{ btnText }}
        </el-button>
      </el-form-item>
    </el-form>
    <el-select v-model="lgSelect" @change="changeLg" style="width: 100px; margin-right: 20px">
      <el-option
        v-for="item in lgOption"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>
  </div>
</template>

<script>
import {
  defineComponent,
  getCurrentInstance,
  reactive,
  toRefs,
  ref,
  computed,
} from 'vue'
import { Login } from '@/api/login'
import { useStore } from 'vuex'
import { useRouter, useRoute } from 'vue-router'
import { useI18n } from 'vue-i18n'
export default defineComponent({
  name: 'login',
  setup() {
    const { proxy: ctx } = getCurrentInstance() // 可以把ctx当成vue2中的this
    const store = useStore()
    const router = useRouter()
    const route = useRoute()
    const {t, locale} = useI18n()
    const state = reactive({
      lgSelect: 'zh',
      lgOption: [
        {
          label: '简体中文',
          value: 'zh'
        },
        {
          label: 'English',
          value: 'en'
        },
        {
          label: 'japen',
          value: 'ja'
        }
      ],
      model: {
        user_cd: '',
        password: '',
      },
      rules: {
        userName: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          {
            min: 6,
            max: 12,
            message: '长度在 6 到 12 个字符',
            trigger: 'blur',
          },
        ],
      },
      loading: false,
      btnText: computed(() => (state.loading ? '登录中...' : t("I18n.LogIn"))),
      loginForm: ref(null),
      submit: () => {
        if (state.loading) {
          return
        }
        state.loginForm.validate(async valid => {
          if (valid) {
            state.loading = true
            const { code, token, msg } = await Login(state.model)
            if (+code === 200) {
              ctx.$message.success({
                message: '登录成功',
                duration: 1000,
              })

              const targetPath = decodeURIComponent(route.query.redirect)
              if (targetPath.startsWith('http')) {
                // 如果是一个url地址
                window.location.href = targetPath
              } else if (targetPath.startsWith('/')) {
                // 如果是内部路由地址
                router.push(targetPath)
              } else {
                router.push('/')
              }
              store.commit('app/setToken', token)
            } else {
              ctx.$message.error(msg)
            }
            state.loading = false
          }
        })
      },
      changeLg (val) {
        locale.value = val
        store.commit('app/setLanguage', val)
      },
    })

    return {
      ...toRefs(state),
      t
    }
  },
})
</script>

<style lang="scss" scoped>
.login {
  transition: transform 1s;
  transform: scale(1);
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: #2d3a4b;
  .form {
    width: 520px;
    max-width: 100%;
    padding: 0 24px;
    box-sizing: border-box;
    margin: 160px auto 0;
    .title {
      color: #fff;
      text-align: center;
      font-size: 24px;
      margin: 0 0 24px;
    }
    .text {
      font-size: 16px;
      :deep(.el-input__inner) {
        border: 1px solid rgba(255, 255, 255, 0.1);
        background: rgba(0, 0, 0, 0.1);
        color: #fff;
        height: 48px;
        line-height: 48px;
        &::placeholder {
          color: rgba(255, 255, 255, 0.2);
        }
      }
    }
    .btn {
      width: 100%;
    }
  }
}
.el-select {
  position: absolute;
  top: 20px;
  right: 20px;
  :deep {
    .el-input__inner {
      border: 0
    }
  }
}
</style>
