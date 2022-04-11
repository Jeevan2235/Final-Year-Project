<template>
  <li>
      <hello />
      <deals />
      <maps />
      <blog />
  </li>
</template>

<script>
import Blog from '../components/blog.vue'
import Deals from '../components/deals.vue'
import hello from '../components/hello.vue'
import Maps from '../components/maps.vue'
export default {
  components: { hello, Maps, Blog },

}
    Deals
</script>

<style>

</style>