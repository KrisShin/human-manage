<!--
 * @Description: 
 * @Version: 
 * @Author: zhendong.wu
 * @Date: 2021-08-25 11:00:18
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-09-01 09:50:06
 * @FilePath: /0825/src/views/admin/index.vue
-->
<template>
  <div>
    <search-box :departments="department" @search="handleSearch"></search-box>

    <div class="table-wrapper">
      <div class="flex flex-col-center flex-row-between">
        <div>
          show
          <b-form-select style="font-size: 14px" v-model="page.pageSize" @change="changePageSize" :options="pageSizeOption"></b-form-select>
          entries
        </div>
        <div class="flex flex-col-center">
          Search
          <el-input @change="SearchChange" v-model="keywords" type="text" style="margin-left: 10px"></el-input>
        </div>
      </div>

      <el-table
        :data="tableData"
        style="width: 100%; margin-bottom: 20px"
        @sort-change="sortChange"
        v-loading="isloading"
      >
        <el-table-column prop="name" sortable label="NAME" ></el-table-column>
        <el-table-column prop="positon" label="POSITION">
          <template slot-scope="{row}">
            <svg-icon icon-class="table-edit" class-name="table-icon" @click="handleClickEdit(row)"></svg-icon>
            <svg-icon icon-class="table-del" class-name="table-icon" @click="handleClickDelete(row)"></svg-icon>  
          </template>
        </el-table-column>
        <el-table-column prop="office" sortable label="OFFICE" show-overflow-tooltip></el-table-column>
        <el-table-column prop="age" sortable label="AGE"></el-table-column>
        <el-table-column prop="create_time" sortable label="START DATE" show-overflow-tooltip></el-table-column>
        <el-table-column prop="salary" sortable label="SALARY"></el-table-column>
      </el-table>

      <div class="flex flex-col-center flex-row-end">
        <el-pagination
          background
          layout="prev, pager, next"
          :total="page.total"
          :page-size="page.pageSize"
          prev-text="Previous"
          next-text="Next"
          @current-change="changePageNumber"
        ></el-pagination>
      </div>
      <p style="text-align: right; margin-top: 15px">
        <el-button type="primary" @click="createUser">追加</el-button>
      </p>
    </div>
    <el-dialog
      :title="isEdit ? '人员信息编辑' : '人员信息追加'"
      :visible.sync="dialogVisible"
    >
      <el-form ref="form" :model="formData" label-width="80px" :rules="rules">
        <el-form-item label="用户id" prop="id" v-if="isEdit">
          <el-input v-model="formData.id" disabled></el-input>
        </el-form-item>
        <el-form-item label="用户名" prop="name">
          <el-input v-model="formData.name"></el-input>
        </el-form-item>
        <el-form-item label="部门" prop="department_id">
          <el-select v-model="formData.department_id" placeholder="请选择" clearable>
            <el-option 
              v-for="item in department"
              :key="item.id"
              :label="item.name" 
              :value="item.id"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-checkbox-group v-model="formData.status">
            <el-checkbox label="在职" name="在职"></el-checkbox>
            <el-checkbox label="休假" name="休假"></el-checkbox>
          </el-checkbox-group>
        </el-form-item>
        <el-form-item label="性别">
          <el-radio-group v-model="formData.gender">
            <el-radio label="男">男</el-radio>
            <el-radio label="女">女</el-radio>
            <el-radio label="不详">不详</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="日期">
          <el-date-picker v-model="formData.create_time" type="datetime" placeholder="请选择"></el-date-picker>
        </el-form-item>
      </el-form>
      <div style="text-align: right">
        <el-button type="primary" @click="submit">保存</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import SearchBox from './components/SearchBox'
import { getUserList, userInfo, getDepartment } from '@/api/admin'
export default {
  name: '',
  props: {

  },
  components: {
    SearchBox
  },
  data () {
    return {
      page: {
        pageSize: 10,
        pageNumber: 1,
        total: 0
      },
      pageSizeOption: [
        {
          value: 5,
          text: '5'
        },
        {
          value: 10,
          text: 10
        },
        {
          value: 20,
          text: '20'
        }
      ],
      keywords: '',
      tableData: [],
      isloading: false,
      isEdit: false,
      dialogVisible: false,
      formData: {
        status: []
      },
      rules: {
        id: [
          {
            required: true,
            message: '请输入用户id',
            trigger: 'blur'
          }
        ],
        name: [
          {
            required: true,
            message: '请输入用户名',
            trigger: 'blur'
          }
        ]
      },
      department: [],
      searchData: {}
    }
  },
  watch: {

  },
  computed: {

  },
  created () {
    this.getDepartmentData()
  },
  mounted () {
    this.getTableData()
  },
  methods: {
    getTableData () {
      const params = {
        page: this.page.pageNumber,
        pageSize: this.page.pageSize,
        ...this.searchData
      }
      this.isloading = true
      getUserList(params)
        .then(res => {
          this.isloading = false
          this.tableData = res.data
          this.page.total = res.total
          this.$forceUpdate()
        })
    },
    getDepartmentData () {
      getDepartment()
        .then(res => {
          this.department = res.data
        })
    },
    actionUser (params, method) {
      userInfo(params, method)
        .then(res => {
          if (method === 'get') {
            this.formData = res.data
            this.formData.status = res.data.status.split(',')
            this.dialogVisible = true
          } else {
            this.$message.success('操作成功')
            this.getTableData()
            this.dialogVisible = false
          }
        })
    },
    handleSearch (data) {
      this.searchData = data
      this.getTableData()
    },
    SearchChange (val) {
      this.searchData.name = val
      this.getTableData()
    },
    changePageSize() {
      this.page.pageNumber = 1
      this.getTableData()
    },
    changePageNumber (number) {
      this.page.pageNumber = number
      this.getTableData()
    },
    sortChange ({column, prop, order}) {

    },
    handleClickEdit (row) {
      this.isEdit = true
      this.actionUser({id: row.id}, 'get')
    },
    handleClickDelete ({id}) {
      const params = {
        id: id
      }
      this.actionUser(params, 'delete')
    },
    createUser () {
      this.isEdit = false
      this.dialogVisible = true
      this.formData = {
        status: []
      }
    },
    submit () {
      this.$refs.form.validate((valid) => {
        if (valid) {
          const params = {...this.formData}
          params.status = params.status.join(',')
          this.actionUser(params, this.isEdit ? 'put' : 'post')
        } else {
          return false;
        }
      })
    }
  }
}
</script>

<style scoped lang="scss">
.table-wrapper {
  padding-top: 20px;
}
.table-icon {
  width: 16px;
  height: 16px;
  margin-right: 10px;
  cursor: pointer;
}
</style>
