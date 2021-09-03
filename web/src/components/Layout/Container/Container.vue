<!--
 * @Description: 
 * @Version: 
 * @Author: zhendong.wu
 * @Date: 2021-08-25 11:43:13
 * @LastEditors: zhendong.wu
 * @LastEditTime: 2021-09-01 10:31:58
 * @FilePath: /0825/src/components/layout/Container/Container.vue
-->
<template>
  <div class="container">
    <div class="history-card" v-if="historyLink.length > 0">
      <div v-for="item in historyLink" :key="item.path" class="tag" @click="goToPath(item.path)">
        <span>{{ item.title }}</span>
        <i class="el-icon-close" @click.stop="delTag(item)"></i>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'Container',
  props: {

  },
  components: {

  },
  data () {
    return {

    }
  },
  watch: {
    '$route': {
      immediate: true,
      handler (route) {
        const data = {
          title: route.meta.title,
          path: route.path
        }
        this.$store.dispatch('GET_AND_SET_HISTORY_LINK', JSON.stringify(data))
      }
    }
  },
  computed: {
    historyLink () {
      return this.$store.state.historyLink
    }
  },
  created () {

  },
  mounted () {

  },
  methods: {
    delTag (tag) {
      this.$store.dispatch('DEL_HISTORY_LINK', JSON.stringify(tag))
    },
    goToPath (path) {
      this.$router.push({path: path})
    }
  }
}
</script>

<style scoped lang="scss">
.container {
  height: 100%;
  width: 260px;
  font-size: 16px;
  color: #666;
  margin-top: 20px;
  margin-left: 20px;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 16px;
  box-shadow: 0 0 3px 0px rgba(0,0,0,.16);
  overflow-y: auto;

  .history-card {
    border-bottom: 1px solid #ddd;
    padding-bottom: 10px;
    margin-bottom: 10px;
    .tag {
      display: inline-block;
      min-width: 110px;
      padding: 5px 20px;
      font-size: 14px;
      color: #fff;
      background-color: #d6d29f;
      margin-right: 10px;
      position: relative;

      i {
        position: absolute;
        top: 50%;
        right: 5px;
        transform: translateY(-50%);
      }
    }
  }
}
</style>
