<template>
  <div id="app" class="max-screen-space-container flex-column-items-centered">
    <router-view>
    </router-view>
  </div>
</template>

<script>

import '../public/style.css'
export default {
  name: 'App',
  components: {
  },
  mounted() {
    this.$store.dispatch("getPatients")
  }
}
</script>

<style>
</style>
