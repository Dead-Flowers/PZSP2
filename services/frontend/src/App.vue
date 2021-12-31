<template>
  <v-app id="app">
    <v-navigation-drawer app v-if="isLoggedIn()">
    </v-navigation-drawer>
    <v-main>
      <v-container fluid>
        <router-view>
        </router-view>
      </v-container>
    </v-main>
    <v-footer app>
    </v-footer>
  </v-app>
</template>

<script>
import router from './router'
export default {
  name: 'App',
  components: {
  },
  methods: {
    isLoggedIn() {
      return this.$store.getters["isLoggedIn"];
    }
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
.app {
  width: 100vw;
  height: 100vh;
}
</style>
