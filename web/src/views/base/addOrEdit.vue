<template>
  <div>
    <p>{{ isEdit === '1' ? '编辑用户' : '新增用户' }}</p>
    <el-form ref="form" label-width="100px" :model="formData" :rules="rules">
      <el-form-item :label="t('I18n.UserCd')" prop="user_cd">
        <el-input v-model="formData.user_cd" :placeholder="t('I18n.UserCd')" :disabled="isEdit === '1'"></el-input>
      </el-form-item>
      <el-form-item :label="t('I18n.Name')" prop="user_nm">
        <el-input v-model="formData.user_nm" :placeholder="t('I18n.Name')"></el-input>
      </el-form-item>
      <el-form-item :label="t('I18n.UserPw')" prop="name">
        <el-input v-model="formData.name" :placeholder="t('I18n.UserPw')"></el-input>
      </el-form-item>
      <el-form-item :label="t('I18n.Sex')" prop="sex">
        <el-radio-group v-model="formData.sex">
          <el-radio :label="1">男</el-radio>
          <el-radio :label="2">女</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item :label="t('I18n.BirthDay')" prop="birthday">
        <el-date-picker
          style="width: 100%"
          v-model="formData.birthday"
          type="date"
          value-format="yyyy-MM-dd"
          :placeholder="t('I18n.BirthDay')"
        ></el-date-picker>
      </el-form-item>
      <el-form-item :label="t('I18n.Email')" prop="email">
        <el-input v-model="formData.email" :placeholder="t('I18n.Email')"></el-input>
      </el-form-item>
      <el-form-item :label="t('I18n.PhoneNo')" prop="phone">
        <el-input v-model="formData.phone" :placeholder="t('I18n.PhoneNo')"></el-input>
      </el-form-item>
      <el-form-item :label="t('I18n.Telephone')" prop="telephone">
        <el-input
          v-model="formData.telephone"
          :placeholder="t('I18n.Telephone')"
        ></el-input>
      </el-form-item>
      <el-form-item :label="t('I18n.Roles')" prop="role_cd">
        <el-select
          v-model="formData.role_cd"
          :placeholder="t('I18n.Roles')"
          style="width: 100%"
          value-key="code_no"
          clearable
        >
          <el-option
            v-for="item in roleOptions"
            :key="item.code_no"
            :label="item.code_nm"
            :value="item"
          ></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="勤务区分" prop="duty_cd">
        <el-select
          v-model="formData.duty_cd"
          placeholder="请选择勤务区分"
          style="width: 100%"
          value-key="code_no"
          clearable
        >
          <el-option
            v-for="item in qingwuOp"
            :key="item.code_no"
            :label="item.code_nm"
            :value="item"
          ></el-option>
        </el-select>
      </el-form-item>
      <el-form-item :label="t('I18n.FactoryNm')" prop="factory_cd">
        <el-select
          v-model="formData.factory_cd"
          :placeholder="t('I18n.FactoryNm')"
          style="width: 100%"
          @change="changeFactory"
          clearable
        >
          <el-option
            v-for="item in factoryOp"
            :key="item.factory_cd"
            :label="item.factory_nm"
            :value="item.factory_cd"
          ></el-option>
        </el-select>
      </el-form-item>
      <el-form-item :label="t('I18n.DepNm')" prop="dep_cd">
        <el-select
          v-model="formData.dep_cd"
          :placeholder="t('I18n.DepNm')"
          style="width: 100%"
          clearable
          :disabled="!formData.factory_cd"
        >
          <el-option
            v-for="item in departmentOp"
            :key="item.dep_cd"
            :label="item.dep_name"
            :value="item.dep_cd"
          ></el-option>
        </el-select>
      </el-form-item>
      <el-form-item :label="t('I18n.Address1')" prop="address1">
        <el-input v-model="formData.address1" :placeholder="t('I18n.Address1')"></el-input>
      </el-form-item>
      <el-form-item :label="t('I18n.Address2')" prop="address2">
        <el-input v-model="formData.address2" :placeholder="t('I18n.Address2')"></el-input>
      </el-form-item>
      <el-form-item :label="t('I18n.Comment')" prop="comment">
        <el-input type="textarea" v-model="formData.comment" :placeholder="t('I18n.Comment')"></el-input>
      </el-form-item>
      <el-form-item :label="t('I18n.Photo')">
        <el-upload
          class="upload-demo"
          :action="uploadUrl"
          :http-request="uploadFile"
          :before-upload="beforeUpload"
          :limit="1"
          :file-list="fileList"
          list-type="picture"
          :on-exceed="exceedUpload"
        >
          <el-button size="small" type="primary">上传</el-button>
        </el-upload>
      </el-form-item>
      <div style="text-align: right">
        <el-button size="small" @click="handleBack">返回</el-button>
        <el-button type="primary" size="small" @click="saveCreate">
          {{t('I18n.Save')}}
        </el-button>
      </div>
    </el-form>
  </div>
</template>
<script>
import moment from 'moment'
import {
  defineComponent,
  reactive,
  toRefs,
  watch,
  onBeforeMount,
  ref,
} from 'vue'
import { useRoute, useRouter } from 'vue-router'
import {
  getDepartment,
  getFactory,
  editUser,
  addUser,
  getRole,
  getQingwu,
  getUserInfo,
  upload,
} from '@/api/user-manege'
import { ElMessage, ElMessageBox } from 'element-plus'
import { useI18n } from 'vue-i18n'
export default defineComponent({
  setup(props, context) {
    const {t} = useI18n()
    const route = useRoute()
    const router = useRouter()
    const form = ref(null)
    const state = reactive({
      formData: {
        factory_cd: '',
        user_cd: '',
        user_nm: '',
        role_cd: null,
        duty_cd: null,
        dep_cd: '',
        comment: '',
        name: '',
        sex: '1',
        birthday: '',
        address1: '',
        address2: null,
        phone: '',
        telephone: null,
        email: '',
        photo: null,
      },
      uploadUrl: 'http://:9100/api/upload/',
      fileList: [],
      roleOptions: [],
      departmentOp: [],
      factoryOp: [],
      qingwuOp: [],
      rules: {
        user_cd: [{ required: true, message: '请输入用户Id', trigger: 'blur' }],
        user_nm: [{ required: true, message: '请输入姓名', trigger: 'blur' }],
        name: [{ required: true, message: '请输入昵称', trigger: 'blur' }],
        sex: [{ required: true, message: '请选择性别', trigger: 'change' }],
        birthday: [
          { required: true, message: '请选择生日', trigger: 'change' },
        ],
        email: [{ required: true, message: '请输入邮箱', trigger: 'blur' }],
        phone: [{ required: true, message: '请输入手机号码', trigger: 'blur' }],
        role_cd: [{ required: true, message: '请选择角色', trigger: 'change' }],
        duty_cd: [
          { required: true, message: '请选择勤务区分', trigger: 'change' },
        ],
        factory_cd: [
          { required: true, message: '请选择工厂', trigger: 'change' },
        ],
        dep_cd: [{ required: true, message: '请选择部门', trigger: 'change' }],
        address1: [{ required: true, message: '请输入住址1', trigger: 'blur' }],
        address2: [{ required: true, message: '请输入住址2', trigger: 'blur' }],
      },
      isEdit: route.params.isEdit,
      saveCreate() {
        state.formData.birthday = moment(state.formData.birthday).format(
          'YYYY-MM-DD'
        )
        form.value.validate(valid => {
          if (valid) {
            if (route.params.isEdit === '1') {
              state.editUserData()
            } else {
              state.createUser()
            }
          } else {
            console.log('error submit!!')
            return false
          }
        })
      },
      changeFactory() {
        state.formData.dep_cd = ''
        state.getDepartmentData()
      },
      getDepartmentData() {
        const params = {
          factory_cd: state.formData.factory_cd,
        }
        getDepartment(params).then(res => {
          if (res.code === 200) {
            state.departmentOp = res.data
          }
        })
      },
      getFactoryData() {
        getFactory().then(res => {
          if (res.code === 200) {
            state.factoryOp = res.data
          }
        })
      },
      getQingwuData() {
        getQingwu().then(res => {
          if (res.code === 200) {
            state.qingwuOp = res.data
          }
        })
      },
      getRoleData() {
        getRole().then(res => {
          if (res.code === 200) {
            state.roleOptions = res.data
          }
        })
      },
      getUserDetail() {
        if (route.params.isEdit === '0') return
        const params = {
          user_cd: route.params.userId,
        }
        getUserInfo(params).then(res => {
          if (res.code === 200) {
            state.formData = res.data
            for (const key in state.formData) {
              if (key === 'factory_cd' || key === 'dep_cd') {
                state.formData[key] = state.formData[key][key]
              }
            }
            if (res.data.photo && res.data.photo !== 'null') {
              state.fileList = [{name: '', url: res.data.photo}]
            }
            state.getDepartmentData()
          }
        })
      },
      createUser() {
        const params = new FormData()
        for (const key in state.formData) {
          if (key === 'role_cd' || key === 'duty_cd') {
            params.append(key, JSON.stringify(state.formData[key]))
          } else {
            params.append(key, state.formData[key])
          }
        }
        addUser(params).then(res => {
          if (res.code === 200) {
            ElMessage.success('保存成功')
            form.value.resetFields()
          } else {
            ElMessage.error(res.message)
          }
        })
      },
      editUserData() {
        const params = new FormData()
        for (const key in state.formData) {
          if (key === 'role_cd' || key === 'duty_cd') {
            params.append(key, JSON.stringify(state.formData[key]))
          } else {
            params.append(key, state.formData[key])
          }
        }
        editUser(params).then(res => {
          if (res.code === 200) {
            ElMessage.success('保存成功')
          } else {
            ElMessage.error(res.message)
          }
        })
      },
      beforeUpload(file) {
        const fileArr = file.name.split('.')
        const fileType = fileArr[fileArr.length - 1]
        const typeList = ['png', 'jpg', 'jpeg', 'gif', 'svg']
        if (typeList.indexOf(fileType) === -1) {
          ElMessage.warning('只能上传图片文件')
          return false
        }
        return true
      },
      uploadFile(file) {
        const params = new FormData()
        params.append('file', file.file)
        upload(params).then(res => {
          if (res.code === 200) {
            state.formData.photo = res.data
            state.fileList = [{name: file.name, url: res.data}]
            ElMessage.success('上传成功')
          } else {
            ElMessage.error('上传失败')
          }
        })
      },
      exceedUpload() {
        ElMessage.error('最多只能上传一张图片，请删除后重新上传')
      },
      initPage() {
        state.getUserDetail()
        state.getFactoryData()
        state.getQingwuData()
        state.getRoleData()
      },
      handleBack() {
        ElMessageBox.confirm(
          '返回后编辑的信息将不会保存，确认返回?',
          '提示',
          {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning',
          }
        )
          .then(() => {
            router.back()
          })
      }
    })
    onBeforeMount(() => {
      state.initPage()
    })
    return {
      ...toRefs(state),
      form,
      t
    }
  },
})
</script>
<style lang="scss" scoped>
.el-form {
  width: 500px;
  background: transparent;
}
.back {
  cursor: pointer;
  &:hover {
    color: #3699ff
  }
}
</style>
