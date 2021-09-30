<template>
  <div>
    <el-form ref="formSearch" label-width="80px" :model="searchForm" size="small">
      <el-row>
        <el-col :span="10">
          <el-form-item :label="t('I18n.UserPw')" prop="name">
            <el-input
              v-model="searchForm.name"
              :placeholder="t('I18n.UserPw')"
            ></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item :label="t('I18n.RoleNm')" prop="role">
            <el-select
              v-model="searchForm.role"
              :placeholder="t('I18n.RoleNm')"
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
        </el-col>
        <el-col :span="10">
          <el-form-item label="有效区分" prop="abort_div">
            <el-select
              v-model="searchForm.abort_div"
              placeholder="请选择有效区分"
              style="width: 100%"
              value-key="code_no"
              clearable
            >
              <el-option
                v-for="item in youxiaoOp"
                :key="item.code_no"
                :label="item.code_nm"
                :value="item"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="勤务区分" prop="duty">
            <el-select
              v-model="searchForm.duty"
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
        </el-col>
        <el-col :span="10">
          <el-form-item label="创建时间" class="m-b0" prop="create_time">
            <el-date-picker
              v-model="searchForm.create_time"
              type="datetimerange"
              range-separator="至"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
              style="width: 100%"
              value-format="YYYY-MM-DD"
            ></el-date-picker>
          </el-form-item>
        </el-col>
        <el-col :span="14" style="text-align: right">
          <el-button
            type="primary"
            size="small"
            icon="el-icon-search"
            @click="getUserTableList"
          >
            {{t('I18n.Search')}}
          </el-button>
          <el-button 
            type="info" 
            size="small" 
            icon="el-icon-refresh"
            @click="resetSearch"
          >
            重置
          </el-button>
        </el-col>
      </el-row>
    </el-form>
    <div class="table-wrapper">
      <div class="table-global-action">
        <span style="font-weight: 500; font-size: 15px">{{t('I18n.UserManagement')}}</span>
        <div>
          <el-button type="primary" size="small" @click="handleAddUser">
            新增
          </el-button>
          <el-button type="danger" size="small" @click="handleDeleteBatch">
            批量删除
          </el-button>
        </div>
      </div>
      <el-table
        ref="userTable"
        :data="tableData"
        tooltip-effect="light"
        style="width: 100%; margin-top: 20px"
        border
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="55"></el-table-column>
        <el-table-column
          :label="t('I18n.UserPw')"
          width="180"
          prop="user_nm"
          sortable
        ></el-table-column>
        <el-table-column
          prop="email"
          :label="t('I18n.Email')"
          width="120"
          sortable
        ></el-table-column>
        <el-table-column
          prop="telephone"
          :label="t('I18n.Telephone')"
          width="120"
          sortable
        ></el-table-column>
        <el-table-column prop="role_cd" sortable :label="t('I18n.RoleNm')" width="120">
          <template #default="{row}">
            {{row.role_cd.code_nm}}
          </template>
        </el-table-column>
        <el-table-column prop="sex" sortable :label="t('I18n.Sex')" width="120">
          <template #default="{row}">
            {{row.sex + '' === '1' ? '男' : '女'}}
          </template>
        </el-table-column>
        <el-table-column
          prop="create_time"
          label="创建时间"
          width="160"
          sortable
        ></el-table-column>
        <el-table-column
          prop="comment"
          :label="t('I18n.Comment')"
          width="160"
          sortable
          show-overflow-tooltip
        ></el-table-column>
        <el-table-column :label="t('I18n.More')" width="180">
          <template #default="{row}">
            <el-button
              type="primary"
              size="mini"
              @click="handleShowUserInfo(row.user_cd)"
            >
              编辑
            </el-button>
            <el-button type="danger" size="mini" @click="handleDeleteUser(row)">
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="paginationConfig.pageNum"
        :page-sizes="paginationConfig.pageSizes"
        :page-size="paginationConfig.pageSize"
        :layout="paginationConfig.layout"
        :total="paginationConfig.total"
      ></el-pagination>
    </div>
    <table-delete
      @close="handleCloseDeleteDialog"
      @submit="handleSubmitDeleteUser"
      :table-data="deleteRowList"
      :columns="delateColumns"
      v-if="dialogVisible"
    ></table-delete>
  </div>
</template>

<script>
import { defineComponent, reactive, ref, toRefs, onMounted } from 'vue'
import TableDelete from '@/components/Dialog/TableDelete.vue'
import { ElMessage } from 'element-plus'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import {
  getUserList,
  getRole,
  getQingwu,
  getYouxiao,
  deleteUser,
} from '@/api/user-manege'
export default defineComponent({
  name: 'BasePage',
  components: {
    TableDelete,
  },
  setup() {
    const router = useRouter()
    const {t} = useI18n()
    const state = reactive({
      searchForm: {
        create_time: [],
      },
      tableData: [],
      deleteRowList: [],
      // 分页配置
      paginationConfig: {
        layout: 'total, prev, pager, next, sizes', // 分页组件显示哪些功能
        pageSize: 10, // 每页条数
        pageSizes: [10, 20, 50, 100],
        style: { textAlign: 'right' },
        pageNum: 1,
        total: 0,
      },
      qingwuOp: [],
      youxiaoOp: [],
      roleOptions: [],
      isEditUser: false,
      dialogVisible: false,
      delateColumns: [
        {
          label: "用户名",
          prop: "user_nm",
          t: 'UserPw'
        },
        {
          label: "邮箱",
          prop: "email",
          t: 'Email'
        },
        {
          label: "电话号码",
          prop: "telephone",
          t: 'Telephone'
        }
      ],
      handleSelectionChange(val) {
        state.deleteRowList = val
      },
      handleSizeChange(size) {
        state.paginationConfig.pageSize = size
        state.paginationConfig.pageNum = 1
        state.getUserTableList()
      },
      handleCurrentChange(num) {
        state.paginationConfig.pageNum = num
        state.getUserTableList()
      },
      handleDeleteBatch() {
        if (state.deleteRowList.length === 0) {
          ElMessage.warning('请勾选删除的数据')
          return
        }
        state.dialogVisible = true
      },
      handleAddUser() {
        state.gotoDetail()
      },
      gotoDetail(id) {
        router.push({
          name: 'UserDetail',
          params: {
            isEdit: id ? '1' : '0',
            userId: id || '-1',
          },
        })
      },
      getUserTableList() {
        const params = {
          page: state.paginationConfig.pageNum,
          pageSize: state.paginationConfig.pageSize,
          name: state.searchForm.name,
          role: state.searchForm.role,
          abort_div: state.searchForm.abort_div,
          duty: state.searchForm.duty,
          start_time: state.searchForm.create_time[0]
            ? state.searchForm.create_time[0]
            : null,
          end_time: state.searchForm.create_time[1]
            ? state.searchForm.create_time[1]
            : null,
        }
        getUserList(params).then(res => {
          if (res.code === 200) {
            state.tableData = res.data
            state.paginationConfig.total = res.total
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
      getYouxiaoData() {
        getYouxiao().then(res => {
          if (res.code === 200) {
            state.youxiaoOp = res.data
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
      handleDeleteUser(row) {
        state.deleteRowList = [row]
        state.dialogVisible = true
      },
      handleCloseDeleteDialog() {
        state.dialogVisible = false
        state.deleteRowList = []
      },
      handleSubmitDeleteUser() {
        const users = state.deleteRowList.map(item => item.id)
        const params = {
          user_cd: users,
        }
        deleteUser(params).then(res => {
          if (res.code === 200) {
            ElMessage.success('删除成功')
            state.getUserTableList()
          }
          state.handleCloseDeleteDialog()
        })
      },
      handleShowUserInfo(id) {
        state.gotoDetail(id)
      },
      async initPage() {
        await state.getQingwuData()
        await state.getYouxiaoData()
        await state.getRoleData()
        await state.getUserTableList()
      },
      resetSearch() {
        formSearch.value.resetFields()
      },
      resetLang(field) {
        return t(`I18n.${field}`)
      }
    })
    onMounted(() => {
      state.initPage()
    })
    const formSearch = ref(null)
    return {
      ...toRefs(state),
      formSearch,
      t
    }
  },
})
</script>
<style lang="scss" scoped>
.el-form {
  padding: 20px;
  background: #fff;
  :deep {
    .el-form-item {
      max-width: 400px
    }
  }
}
.m-b0 {
  margin-bottom: 0;
}
.table-wrapper {
  background: #fff;
  padding: 20px;
  margin-top: 14px;
}
.table-global-action {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.el-table {
  :deep {
    thead {
      color: #333;
      font-weight: 700;
    }
    th {
      font-weight: 500;
      background: #f5f5f5;
    }
  }
}
.el-pagination {
  text-align: right;
  margin-top: 10px;
  :deep {
    .el-pagination__sizes {
      margin-right: 0;
      .el-input {
        margin-right: 0;
      }
    }
  }
}
</style>
