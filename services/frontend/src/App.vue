<template>
  <v-app id="app">
    <Navbar v-if="isLoggedIn" />
    <v-main>
      <v-container fluid>
        <router-view/>
        <v-snackbar
        v-model="snackbar"
        :multi-line="true"
        >
          {{ text }}

          <template v-slot:action="{ attrs }">
            <v-btn
              color="red"
              text
              v-bind="attrs"
              @click="closeSnackbar"
            >
            Close
            </v-btn>
          </template>
        </v-snackbar>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import router from './router'
import Navbar from "./components/Navbar.vue"
export default {
  name: 'App',
  components: {
    Navbar,
  },
  methods: {
    closeSnackbar() {
      this.$store.commit('closeSnackbar')
    }
  },
  computed: {
    snackbar() {
      return this.$store.getters["isSnackbarOpened"]
    },
    text() {
      return this.$store.getters["snackbarText"]
    },
    isLoggedIn() {
      // porbaly needed to fix, not routing sometimes
      if(this.$route.name == 'WelcomePage' && this.$store.getters["isLoggedIn"]){
        router.push(`/${this.$store.getters["userType"]}/home`)
      }

      return this.$store.getters["isLoggedIn"];
    },
  },
  async beforeMount() {
    // this needs to be here so routing dosen't gets messed up
    await this.$store.dispatch("actionCheckLoggedIn")
  },
  async mounted() {
    if(this.$route.name == 'WelcomePage' && this.$store.getters["isLoggedIn"]){
      router.push(`/${this.$store.getters["userType"]}/home`)
    }
  },
}
</script>

<style>
.app {
  width: 100vw;
  height: 100vh;
}
</style>
