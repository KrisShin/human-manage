<!--
 * _______________#########_______________________ 
 * ______________############_____________________ 
 * ______________#############____________________ 
 * _____________##__###########___________________ 
 * ____________###__######_#####__________________ 
 * ____________###_#######___####_________________ 
 * ___________###__##########_####________________ 
 * __________####__###########_####_______________ 
 * ________#####___###########__#####_____________ 
 * _______######___###_########___#####___________ 
 * _______#####___###___########___######_________ 
 * ______######___###__###########___######_______ 
 * _____######___####_##############__######______ 
 * ____#######__#####################_#######_____ 
 * ____#######__##############################____ 
 * ___#######__######_#################_#######___ 
 * ___#######__######_######_#########___######___ 
 * ___#######____##__######___######_____######___ 
 * ___#######________######____#####_____#####____ 
 * ____######________#####_____#####_____####_____ 
 * _____#####________####______#####_____###______ 
 * ______#####______;###________###______#________ 
 * ________##_______####________####______________ 
 * 
 * @Descripttion: 
 * @version: 
 * @Date: 2021-04-20 11:06:21
 * @LastEditors: huzhushan@126.com
 * @LastEditTime: 2021-07-23 17:22:14
 * @Author: huzhushan@126.com
 * @HomePage: https://huzhushan.gitee.io/vue3-element-admin
 * @Github: https://github.com/huzhushan/vue3-element-admin
 * @Donate: https://huzhushan.gitee.io/vue3-element-admin/donate/
 -->

<template>
  <el-breadcrumb
    separator-class="el-icon-arrow-right"
    class="breadcrumb"
    :class="{
      mobile: device === 'mobile',
      show: isHorizontalMenu,
      hide: breadcrumbs.length <= 1,
    }"
  >
    <el-breadcrumb-item
      v-for="(item, index) in breadcrumbs"
      :key="index"
      :class="{ no_link: index === breadcrumbs.length - 1 }"
      :to="index < breadcrumbs.length - 1 ? item.path : ''"
    >
      {{ item.meta.t ? l(item.meta.t) : item.meta.title }}
    </el-breadcrumb-item>
  </el-breadcrumb>
</template>
<script>
import { defineComponent, computed, ref, onBeforeMount, watch, reactive, toRefs } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'
import {useI18n} from 'vue-i18n'
export default defineComponent({
  setup(props, { emit }) {
    const {t} = useI18n()
    const store = useStore()
    const device = computed(() => store.state.app.device)
    const router = useRouter()
    const route = router.currentRoute // 这里不使用useRoute获取当前路由，否则下面watch监听路由的时候会有警告
    const breadcrumbs = ref([])
    const defaultSettings = computed(() => store.state.layoutSettings)
    const isHorizontalMenu = computed(
      () => defaultSettings.value.menus.mode === 'horizontal'
    )

    const getBreadcrumbs = route => {
      const home = [{ path: '/', meta: { title: '首页', t: 'Home'} }]
      if (route.name === 'home') {
        return home
      } else {
        const matched = route.matched.filter(
          item => !!item.meta && !!item.meta.title
        )

        return [...home, ...matched]
      }
    }

    onBeforeMount(() => {
      breadcrumbs.value = getBreadcrumbs(route.value)
    })

    watch(
      route,
      newRoute => {
        breadcrumbs.value = getBreadcrumbs(newRoute)
        emit('on-breadcrumbs-change', breadcrumbs.value.length > 1)
      },
      {
        immediate: true,
      }
    )
    const state = reactive({
      l(field) {
        return t(`I18n.${field}`)
      }
    })

    return {
      ...toRefs(state),
      device,
      breadcrumbs,
      isHorizontalMenu,
      t
    }
  },
})
</script>

<style lang="scss" scoped>
.breadcrumb {
  margin-left: 10px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  ::v-deep(a),
  ::v-deep(.is-link) {
    font-weight: normal;
  }
  ::v-deep(.el-breadcrumb__item) {
    float: none;
  }
  .no_link {
    ::v-deep(.el-breadcrumb__inner) {
      color: #97a8be !important;
    }
  }
  &.mobile {
    display: none;
  }
  &.show {
    display: block;
    margin: 0;
    padding: 16px;
    background: #f5f5f5;
  }
  &.hide {
    display: none;
  }
}
</style>
<style lang="scss">
.el-breadcrumb__inner {
  &.is-link,
  a {
    color: #5c5c5c;
  }
}
</style>
