<!--
 * @Description: 
 * @Version: 
 * @Author: zhendong.wu
 * @Date: 2021-08-27 20:55:09
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-09-02 10:52:57
 * @FilePath: /0825/src/components/Layout/Sidebar/menu.vue
-->
<template>
  <div class="menu">


      <!-- <b-nav-item-dropdown 
        bottom
        :class="{'menu-hidden': isHidden}"
        :key="item.path" 
        v-else-if="item.children && item.children.length > 0" 
      >
        <template slot="button-content">
          <span :class="{'hidden': isHidden}">
            <svg-icon :icon-class="item.meta.icon" class-name="menu-icon"></svg-icon>
            {{ item.meta.title }}
          </span>
        </template>
        <b-dropdown-item>
          <menu-list :menu="item.children" class="submenu"></menu-list>
        </b-dropdown-item>
      </b-nav-item-dropdown> -->

    <el-menu
      :default-active="$route.path"
      class="el-menu-vertical"
      :collapse="isHidden"
      :collapse-transition="false"
      @select="handleSelectMenu"
    >
      <template v-for="item in menuData">
        <el-submenu :index="item.path" :key="item.path" v-if="item.children && item.children.length > 0">
          <template slot="title">
            <i class="el-icon-menu"></i>
            <span>{{item.meta.title}}</span>
          </template>
          <el-menu-item 
            :index="item.path === '/' ? '/' + sub.path : item.path  + '/' + sub.path" 
            v-for="sub in item.children" 
            :key="sub.path"
          >{{sub.meta.title}}</el-menu-item>
        </el-submenu>
        <el-menu-item :index="item.path" :key="item.path" v-else>
          <i class="el-icon-menu"></i>
          <span slot="title">{{item.meta.title}}</span>
        </el-menu-item>
      </template>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'MenuList',
  props: {
    menu: {
      type: Array,
      default: []
    },
    isHidden: {
      type: Boolean,
      default: false
    }
  },
  components: {

  },
  data () {
    return {
      menuData: []
    }
  },
  watch: {
    menu: {
      immediate: true,
      handler (list) {
        this.menuData = list
      }
    }
  },
  created () {
    
  },
  methods: {
    handleSelectMenu (path) {
      this.$router.push({path: path})
    }
  }
}
</script>

<style scoped lang="scss">
.menu {
  font-size: 16px;
  .el-menu {
    border-right: 0;
  }
  
  .is-actived {
    color: #3699ff;
  }
  .hidden {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  .menu-hidden {
    
  }
}
</style>
