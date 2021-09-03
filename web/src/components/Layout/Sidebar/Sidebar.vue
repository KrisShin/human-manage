<!--
 * @Description: 
 * @Version: 
 * @Author: zhendong.wu
 * @Date: 2021-08-25 11:43:27
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-09-02 10:49:27
 * @FilePath: /0825/src/components/layout/Sidebar/Sidebar.vue
-->
<template>
  <div class="sidebar" :class="{hidden: isHiddenSidebar}">
    <p style="color: #999" class="title">Main</p>
    
    <menu-list :menu="sidebarMenuList" :isHidden="isHiddenSidebar"></menu-list>
  </div>
</template>

<script>
import MenuList from './Menu'
export default {
  name: 'Sidebar',
  props: {

  },
  components: {
    MenuList
  },
  data () {
    return {
    }
  },
  watch: {
    '$router.options.routes' (routers) {
      this.filterRouterIsNotHidden(routers)
    }
  },
  computed: {
    isHiddenSidebar () {
      return this.$store.state.sidebarHidden
    },
    sidebarMenuList () {
      const routers = this.$router.options.routes
      return this.filterRouterIsNotHidden(routers)
    }
  },
  created () {
    
  },
  methods: {
    filterRouterIsNotHidden (routes) {
      return routes.filter(item => {
        if (item.children) this.filterRouterIsNotHidden(item.children)
        if (!item.hidden) return true
      })
    }
  }
}
</script>

<style scoped lang="scss">
.hidden {
  .title {
    text-align: center;
  }
}
</style>
