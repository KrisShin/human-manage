<!--
 * @Description: 
 * @Author: zhendong.wu
 * @Date: 2021-09-21 23:19:40
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-09-30 09:59:16
-->
<template>
  <el-dialog
    title="确定要删除吗？"
    v-model="dialogShow"
    width="60%"
    :before-close="handleClose"
  >
    <el-table ref="userTable" :data="tableData" style="width: 100%">
      
      <el-table-column
        v-for="(c, index) in columns"
        :key="index"
        :label="c.t ? t(`I18n.${c.t}`) : c.label"
        :prop="c.prop"
      ></el-table-column>
    </el-table>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="handleCancel" size="small">取 消</el-button>
        <el-button type="primary" size="small" @click="handleSubmit">
          {{t('I18n.Save')}}
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>
<script>
import { defineComponent, reactive, toRefs } from 'vue'
import { useI18n } from 'vue-i18n'
export default defineComponent({
  props: {
    tableData: {
      type: Array,
      default: () => [],
    },
    columns: {
      type: Array,
      required: true
    }
  },
  setup(props, context) {
    const {t} = useI18n()
    const state = reactive({
      dialogShow: true,
      handleCancel() {
        context.emit('close', false)
      },
      handleClose() {
        state.handleCancel()
      },
      handleSubmit() {
        context.emit('submit')
      },
    })

    return {
      ...toRefs(state),
      t
    }
  },
})
</script>
