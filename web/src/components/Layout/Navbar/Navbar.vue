<!--
 * @Description: 
 * @Version: 
 * @Author: zhendong.wu
 * @Date: 2021-08-25 11:43:20
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-09-01 09:40:48
 * @FilePath: /0825/src/components/layout/Navbar/Navbar.vue
-->
<template>
  <div class="navbar flex flex-col-center flex-row-between">
    <div class="flex-f1 flex flex-col-center">
      <svg-icon icon-class="navbar-hid" class-name="navbar-icon navbar-menu-show" @click="handleHiddenSidebar"></svg-icon>
      <img src="../../../assets/images/logo.png" width="30px" alt="logo" class="logo">
      <span class="app-name">{{ office }} {{ department }}</span>
    </div>
    <div class="flex-f1 flex flex-col-center flex-row-end">
      <svg-icon icon-class="navbar-search" class-name="navbar-icon"></svg-icon>
      <span class="tags flex flex-col-center flex-row-center">3</span>
      <b-nav-item-dropdown bottom class="user-info">
        <template slot="button-content">{{ username }}</template>
        <b-dropdown-item href="#" @click="handleLogout">Logout</b-dropdown-item>
      </b-nav-item-dropdown>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Navbar',
  props: {

  },
  components: {

  },
  data () {
    return {

    }
  },
  watch: {

  },
  computed: {
    username () {
      return this.$store.state.userinfo?.name
    },
    office () {
      return this.$store.state.userinfo?.office
    },
    department () {
      return this.$store.state.userinfo?.department
    }
  },
  created () {

  },
  mounted () {

  },
  methods: {
    handleLogout () {
      this.$store.state.userinfo = null
      this.$router.push({name: 'Login'})
    },
    handleHiddenSidebar () {
      this.$store.commit('SET_SIDEBAR_IS_HIDDEN', !this.$store.state.sidebarHidden)
    }
  }
}
</script>

<style scoped lang="scss">

</style>
