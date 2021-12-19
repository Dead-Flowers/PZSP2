<template>
  <div id="app" class="max-screen-space-container flex-column-items-centered">
    <router-view>
    </router-view>
  </div>
</template>

<script>

import '../public/style.css'
import router from './router'
export default {
  name: 'App',
  components: {
  },
  async mounted() {
    await this.$store.dispatch("actionCheckLoggedIn")
    
    // TODO: check route for login, use route gourade 
    if(this.$route.name == 'WelcomePage' && this.$store.getters["isLoggedIn"]){
      router.push(`/${this.$store.getters["userType"]}/home`)
    }
  }
}
</script>

<style>
</style>
