<!--
 * @Description: 
 * @Version: 
 * @Author: zhendong.wu
 * @Date: 2021-08-25 10:53:14
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-09-01 09:41:39
 * @FilePath: /0825/src/components/layout/index.vue
-->
<template>
  <div style="height: 100%">
    <navbar></navbar>
    <div class="flex flex-col-start flex-row-between content">
      <sidebar class="flex-f0"></sidebar>
      <container class="flex-f1"></container>
    </div> 
  </div>
</template>

<script>
import Navbar from './Navbar/Navbar'
import Sidebar from './Sidebar/Sidebar'
import Container from './Container/Container'

export default {
  name: 'Layout',
  props: {
    
  },
  components: {
    Navbar,
    Sidebar,
    Container
  
  },
  data () {
    return {

    }
  },
  watch: {

  },
  computed: {

  },
  created () {

  },
  mounted () {

  },
  methods: {

  }
}
</script>

<style scoped lang="scss">
.content {
  height: calc(100% - 100px);
}
</style>
