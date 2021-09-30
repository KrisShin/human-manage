<template>
  <div>
    <el-form label-width="60px" :model="searchForm" size="small" ref="searchform">
      <el-row :gutter="10">
        <el-col :span="6">
          <el-form-item label="类名" prop="class_name">
            <el-input
              v-model="searchForm.class_name"
              placeholder="类名"
            ></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item label="表名" prop="tbl_name">
            <el-input
              v-model="searchForm.tbl_name"
              placeholder="表名"
            ></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item label="表编号" prop="tbl_code">
            <el-input
              v-model="searchForm.tbl_code"
              placeholder="表编号"
            ></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="6" style="text-align: right">
          <el-button
            type="primary"
            size="small"
            icon="el-icon-search"
            @click="getTableDataList"
          >
            {{t('I18n.Search')}}
          </el-button>
          <el-button type="info" size="small" icon="el-icon-refresh" @click="handleResetSearch">
            重置
          </el-button>
        </el-col>
      </el-row>
    </el-form>
    <div class="table-wrapper">
      <div class="table-global-action">
        <span style="font-weight: 500; font-size: 15px">数据库维护</span>
        <div>
          <el-button type="primary" size="small" @click="handleAddTable">
            新增
          </el-button>
          <el-button type="danger" size="small" @click="handleDeleteBatch">
            批量删除
          </el-button>
          <el-button type="primary" size="small" @click="handleDownLoad">
            导出
          </el-button>
        </div>
      </div>
      <el-table
        ref="userTable"
        :data="tableData"
        style="width: 100%"
        border
        @selection-change="handleSelectionChange"
      >
        <el-table-column type="selection" width="55"></el-table-column>
        <el-table-column
          label="类名"
          prop="class_name"
        ></el-table-column>
        <el-table-column
          prop="tbl_name"
          label="表名"
        ></el-table-column>
        <el-table-column
          prop="tbl_code"
          label="表编号"
        ></el-table-column>
        <el-table-column label="操作" width="180">
          <template #default="{row}">
            <el-button
              type="primary"
              size="mini"
              @click="handleEditTable(row)"
            >
              编辑
            </el-button>
            <el-button type="danger" size="mini" @click="handleDeleteTable(row)">
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
      @submit="handleSubmitDeleteTable"
      :table-data="deleteRowList"
      :columns="deleteColumns"
      v-if="dialogVisible"
    ></table-delete>
    <el-dialog
      v-model="isShowCreateDialog"
      :title="!isEdit ? '新建' : '编辑'"
      width="70%"
      @close="getTableDataList"
    >
      <div>
        <el-form 
          ref="form" 
          :model="createForm" 
          label-position="left" 
          label-width="53px"
          :rules="rules"
        >
          <el-row :gutter="20">
            <el-col :span="8">
              <el-form-item label="表名" style="margin-bottom:0" prop="tbl_name">
                <el-input v-model="createForm.tbl_name" :disabled="isEdit" size="small"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="表ID" style="margin-bottom:0" prop="tbl_code">
                <el-input v-model="createForm.tbl_code" :disabled="isEdit" size="small"></el-input>
              </el-form-item>
            </el-col>
            <el-col :span="8">
              <el-form-item label="类名" style="margin-bottom:0" prop="class_name">
                <el-input v-model="createForm.class_name" :disabled="isEdit" size="small"></el-input>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
        <div style="text-align: right; margin-bottom: 10px">
          <el-button type="primary" size="small" @click="createNewRow">新增</el-button>
        </div>
        <el-table
          :data="createTable"
          tooltip-effect="light"
          style="width: 100%"
          height="350"
          border
        >
          <el-table-column
            label="字段名称"
            width="180"
            prop="field_name"
          >
            <template #default="{row, $index}">
              <span v-if="editIndex !== $index">{{ row.field_name }}</span>
              <el-input v-else size="small" v-model="createForm.field_name"></el-input>
            </template>
          </el-table-column>
          <el-table-column
            prop="field_code"
            label="字段编号"
            width="120"
          >
            <template #default="{row, $index}">
              <span v-if="editIndex !== $index">{{ row.field_code }}</span>
              <el-input :disabled="isEditField" v-else size="small" v-model="createForm.field_code"></el-input>
            </template>
          </el-table-column>
          <el-table-column
            prop="type"
            label="字段类型"
            width="120"
          >
            <template #default="{row, $index}">
              <span v-if="editIndex !== $index">{{ row.type }}</span>
              <el-input v-else size="small" v-model="createForm.type"></el-input>
            </template>
          </el-table-column>
          <el-table-column
            prop="decimal"
            label="小数位数"
            width="120"
          >
            <template #default="{row, $index}">
              <span v-if="editIndex !== $index">{{ row.decimal }}</span>
              <el-input type="number" v-else size="small" v-model="createForm.decimal"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="size" label="大小" width="120">
            <template #default="{row, $index}">
              <span v-if="editIndex !== $index">{{ row.size }}</span>
              <el-input v-else type="number" size="small" v-model="createForm.size"></el-input>
            </template>
          </el-table-column>
          <el-table-column
            prop="key"
            label="Key"
            width="160"
          >
            <template #default="{row, $index}">
              <span v-if="editIndex !== $index">{{ row.key }}</span>
              <el-select v-else size="small" v-model="createForm.key">
                <el-option label="0" value="0"></el-option>
                <el-option label="1" value="1"></el-option>
              </el-select>
            </template>
          </el-table-column>
          <el-table-column
            prop="nullable"
            label="Null"
            width="160"
            show-overflow-tooltip
          >
            <template #default="{row, $index}">
              <span v-if="editIndex !== $index">{{ row.nullable === '0' ? '是' : '否' }}</span>
              <el-select v-else size="small" v-model="createForm.nullable">
                <el-option label="是" value="0"></el-option>
                <el-option label="否" value="1"></el-option>
              </el-select>
            </template>
          </el-table-column>
          <el-table-column
            prop="doc"
            label="说明"
            width="160"
            show-overflow-tooltip
          >
            <template #default="{row, $index}">
              <span v-if="editIndex !== $index">{{ row.doc }}</span>
              <el-input v-else size="small" v-model="createForm.doc"></el-input>
            </template>
          </el-table-column>
          <el-table-column
            prop="comment"
            label="备注"
            width="160"
            show-overflow-tooltip
          >
            <template #default="{row, $index}">
              <span v-if="editIndex !== $index">{{ row.comment }}</span>
              <el-input v-else size="small" v-model="createForm.comment"></el-input>
            </template>
          </el-table-column>
          <el-table-column label="操作" width="180">
            <template #default="{row, $index}">
              <el-button
                type="primary"
                size="mini"
                @click="handleSaveField(row)"
                v-if="editIndex === $index"
              >
                {{t('I18n.Save')}}
              </el-button>
              <el-button
                type="primary"
                size="mini"
                @click="handleCancelCreateField"
                v-if="editIndex === $index"
              >
                取消
              </el-button>
              <el-button
                type="primary"
                size="mini"
                @click="handleEditField(row, $index)"
                v-if="editIndex !== $index"
              >
                编辑
              </el-button>
              <el-button 
                type="danger" 
                size="mini" 
                @click="handleDeleteField(row)"
                v-if="editIndex !== $index"
              >
                删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="isShowCreateDialog = false" size="small">取消</el-button>
          <el-button type="primary" size="small" @click="isShowCreateDialog = false">
            确认
          </el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script>
import { defineComponent, reactive, ref, toRefs, onMounted, nextTick } from 'vue'
import TableDelete from '@/components/Dialog/TableDelete.vue'
import { ElMessage } from 'element-plus'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { 
  getTableList,
  createDataField,
  editDataField,
  deleteDataField,
  getFieldTableList,
  getExcel
} from '@/api/database'
export default defineComponent({
  name: 'BasePage',
  components: {
    TableDelete,
  },
  setup() {
    const form = ref(null)
    const searchform = ref(null)
    const router = useRouter()
    const {t} = useI18n()
    const state = reactive({
      // 分页配置
      paginationConfig: {
        layout: 'total, prev, pager, next, sizes', // 分页组件显示哪些功能
        pageSize: 10, // 每页条数
        pageSizes: [10, 20, 50, 100],
        style: { textAlign: 'right' },
        pageNum: 1,
        total: 0,
      },
      searchForm: {},
      tableData: [],
      deleteRowList: [],
      isEdit: false,
      dialogVisible: false,
      isShowCreateDialog: false,
      createForm: {},
      createTable: [],
      editIndex: -1,
      isEditField: false,
      rules: {
        tbl_name: [{required: true, message: '表名不能为空', trigger: 'blur'}],
        tbl_code: [{required: true, message: '表ID不能为空', trigger: 'blur'}],
        class_name: [{required: true, message: '类名不能为空', trigger: 'blur'}]
      },
      editTableInfo: null,
      editFieldInfo: null,
      deleteColumns: [
        {
          prop: 'class_name',
          label: '类名'
        },
        {
          prop: 'tbl_name',
          label: '表名'
        },
        {
          prop: 'tbl_code',
          label: '表编号'
        }
      ],
      deleteRowData: [],
      createNewRow() {
        if (state.editIndex >= 0) {
          ElMessage.warning('当前正在编辑，请保存后再添加！')
          return;
        }
        nextTick(() => {
          state.createTable.unshift({
            field_code: '',
            field_name: '',
            type: '',
            size: '',
            decimal: '',
            nullable: '1',  // 0:true, 1:false
            doc: '',
            key: '1',
            comment: ''
          })
        })
        state.isEditField = false
        state.editIndex = 0
      },
      createFieldData () {
        createDataField(state.createForm).then(res => {
          if (res.code === 200) {
            state.editIndex = -1
            state.createTable[0] = res.data
            state.resetFields()
            ElMessage.success('保存成功')
          } else {
            ElMessage.success(res.msg)
          }
        })
      },
      editFieldData () {
        editDataField(state.createForm).then(res => {
          if (res.code === 200) {
            state.editIndex = -1
            state.resetFields()
            state.getFieldList(state.editTableInfo.tbl_code)
            ElMessage.success('编辑成功')
          } else {
            ElMessage.success(res.msg)
          }
        })
      },
      resetFields () {
        state.createForm.field_code = '',
        state.createForm.field_name = '',
        state.createForm.type = '',
        state.createForm.size = '',
        state.createForm.decimal = '',
        state.createForm.nullable = '1',  // 0:true, 1:false
        state.createForm.key = '1'
        state.createForm.doc = '',
        state.createForm.comment = ''
      },
      deleteFieldData (params) {
        deleteDataField(params).then(res => {
          ElMessage.success('删除成功')
          if (state.tableType === 'table_list') {
            state.getTableDataList()
          } else {
            state.getFieldList(state.editTableInfo.tbl_code)
          }
          state.handleCloseDeleteDialog()
        })
      },
      getFieldList (tbl_code) {
        getFieldTableList({tbl_code}).then(res => {
          if (res.code === 200) {
            state.createTable = res.data
            state.createForm = this.editTableInfo
          }
        })
      },
      handleSelectionChange(val) {
        state.deleteRowList = val
      },
      handleDeleteBatch() {
        if(state.deleteRowList.length === 0) {
          ElMessage.warning('请勾选后再删除')
          return
        }
        state.tableType = 'table_list'
        state.dialogVisible = true
      },
      handleSizeChange(size) {
        state.paginationConfig.pageSize = size
        state.paginationConfig.pageNum = 1
        state.getTableDataList()
      },
      handleCurrentChange(num) {
        state.paginationConfig.pageNum = num
        state.getTableDataList()
      },
      handleAddTable() {
        state.isShowCreateDialog = true
        state.isEdit = false
      },
      getTableDataList() {
        state.editIndex = -1
        const params = {
          class_name: state.searchForm.class_name,
          tbl_name: state.searchForm.tbl_name,
          tbl_code: state.searchForm.tbl_code,
        }
        getTableList(params).then(res => {
          if (res.code === 200) {
            state.tableData = res.data
            state.paginationConfig.total = res.total
          }
        })
      },
      handleSaveField () {
        if (!state.createForm.field_name || !state.createForm.field_code) {
          ElMessage.warning('字段名称和字段编号不能为空！')
          return false
        }
        form.value.validate(valid => {
          if (valid) {
            if (!state.isEditField) {
              state.createFieldData()
            } else {
              state.editFieldData()
            }
          } else {
            return false
          }
        })
      },
      handleDeleteTable(row) {
        state.deleteRowList = [row]
        state.dialogVisible = true
        state.tableType = 'table_list'
      },
      handleCloseDeleteDialog() {
        state.dialogVisible = false
        state.deleteRowList = []
      },
      handleSubmitDeleteTable() {
        const params = {
          [state.tableType]: state.deleteRowList,
        }
        state.deleteFieldData(params)
      },
      handleEditTable(row) {
        state.editTableInfo = row
        state.isEdit = true
        state.isShowCreateDialog = true
        state.getFieldList(row.tbl_code)
      },
      handleEditField(row, idx) {
        if (state.editIndex >= 0) {
          ElMessage.warning('当前正在编辑，请保存后再编辑！')
          return;
        }
        state.isEditField = true
        state.editIndex = idx
        state.createForm = row
      },
      handleCancelCreateField () {
        state.editIndex = -1
        if (!state.isEditField) {
          state.createTable.shift()
          state.resetFields()
        }
      },
      handleDeleteField(row) {
        state.deleteRowList = [row]
        state.dialogVisible = true
        state.tableType = 'field_list'
      },
      async initPage() {
        await state.getTableDataList()
      },
      handleResetSearch () {
        searchform.value.resetFields()
      },
      handleDownLoad () {
        if (state.deleteRowList.length === 0) {
          ElMessage.warning('请勾选后导出')
          return
        }
        const tblCodeList = state.deleteRowList.map(item => item.tbl_code)
        getExcel({table_code_list: tblCodeList}).then(res => {
          const downloadUrl = `http://101.35.152.20:9100/static/${res.data}.xlsx`
          var a = document.createElement("a"); //创建一个<a></a>标签
          a.href = downloadUrl; // 将流文件写入a标签的href属性值
          a.download = "数据表.xlsx"; //设置文件名
          a.style.display = "none";  // 障眼法藏起来a标签
          document.body.appendChild(a); // 将a标签追加到文档对象中
          a.click(); // 模拟点击了a标签，会触发a标签的href的读取，浏览器就会自动下载了
          a.remove();
        })
      }
    })
    onMounted(() => {
      state.initPage()
    })
    return {
      ...toRefs(state),
      form,
      searchform,
      t
    }
  },
})
</script>
<style lang="scss" scoped>
.el-form {
  padding: 20px;
  background: #fff;
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
  margin-top: 20px;
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
.el-dialog {
  :deep .el-dialog__body {
    padding-top: 0;
  }
}
</style>
