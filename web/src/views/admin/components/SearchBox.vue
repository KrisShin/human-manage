<!--
 * @Description: 人员列表搜索条件区域
 * @Version: 
 * @Author: zhendong.wu
 * @Date: 2021-08-28 22:12:22
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-09-01 09:49:58
 * @FilePath: /0825/src/views/admin/components/SearchBox.vue
-->
<template>
  <div class="search-wrapper">
    <b-form class="row form-inline" inline>
      <b-form-group
        label="用户名"
        label-for="input-1"
        class="col-md-6 flex flex-col-center"
      >
        <b-form-input
          id="input-1"
          v-model="formData.name"
          type="text"
          placeholder="请输入"
        ></b-form-input>
      </b-form-group>

      <b-form-group label="性别" class="col-md-6 flex flex-col-center">
        <b-form-radio-group v-model="formData.gender" class="flex flex-col-center flex-row-start" id="checkboxes-4">
          <b-form-radio class="flex flex-col-center flex-row-start" value="男">男</b-form-radio>
          <b-form-radio class="flex flex-col-center flex-row-start" value="女">女</b-form-radio>
          <b-form-radio class="flex flex-col-center flex-row-start" :value="null">全部</b-form-radio>
        </b-form-radio-group>
      </b-form-group>

      <b-form-group label="部门" label-for="input-3" class="col-md-6 flex flex-col-center">
        <el-select
          id="input-3"
          v-model="formData.department_id"
          placeholder="请选择"
          clearable
        >
          <el-option 
            v-for="item in departments"
            :key="item.id"
            :label="item.name" 
            :value="item.id"
          ></el-option>
        </el-select>
      </b-form-group>

      <b-form-group id="input-group-4" class="col-md-6 flex flex-col-center">
        <b-form-checkbox-group v-model="formData.status" id="checkboxes-4" class="flex flex-col-center flex-row-start">
          <b-form-checkbox class="flex flex-col-center flex-row-start" value="在职">在职</b-form-checkbox>
          <b-form-checkbox class="flex flex-col-center flex-row-start" value="休假">休假</b-form-checkbox>
        </b-form-checkbox-group>
      </b-form-group>

      <b-form-group label="日期" class="col-md-6 flex flex-col-center">
        <el-date-picker v-model="formData.create_time" type="datetime" placeholder="请选择"></el-date-picker>
      </b-form-group>
      
      <div class="col-md-6" style="text-align: right"> 
        <el-button  @click="onSubmit" type="primary">检索</el-button>
      </div>
    </b-form>
  </div>
</template>

<script>
export default {
  name: 'SearchBox',
  props: {
    departments: {
      type: Array,
      default: () => []
    }
  },
  data () {
    return {
      formData: {
        status: []
      }
    }
  },
  methods: {
    onSubmit () {
      const params = {...this.formData}
      params.status = this.formData.status
      this.$emit('search', this.formData)
    }
  }
}
</script>

<style scoped lang="scss">
.search-wrapper {
  font-size: 14px;
  padding-bottom: 20px;
  border-bottom: 1px solid #ddd;
  .form-group {
    height: 40px;
    margin-bottom: 20px;
  }
  .btn {
    width: 80px;
    font-size: 14px;
    padding: 5px 10px;
  }
  /deep/legend {
    width: 70px;
    margin-bottom: 0;
    padding-bottom: 0;
  }
  /deep/.custom-control-label {
    width: auto;
    margin: 0 20px 0 5px
  }
  /deep/ label {
    width: 70px;
    flex-shrink: 0;
  }
  /deep/ .form-control {
    font-size: 14px;
    &:focus {
      box-shadow: none;
    }
  }
  /deep/ .custom-select {
    display: block;
    width: 100%;
    padding: 5px 10px;
    font-size: 1rem;
    font-weight: 400;
    color: #212529;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid #ced4da;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    border-radius: 0.25rem;
    transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    &:focus-visible {
      outline: 0;
    }
  }
}
</style>
