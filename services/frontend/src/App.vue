<template>
  <v-app id="app">
    <Navbar v-if="isLoggedIn" />
    <v-main>
      <v-layout align-center justify-center fill-height>
        <router-view />
      </v-layout>
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
    </v-main>
  </v-app>
</template>

<script>
import router from './router'
import Vue from "vue";
import Navbar from "./components/Navbar.vue"
import WS_URL from "./config";
import { getLocalToken } from "./store/user";
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
      return this.$store.getters["isLoggedIn"];
    },
  },
  watch: {
    isLoggedIn(newValue) {  
      if(newValue) {
        if(this.$route.name == 'WelcomePage'){
          router.push(`/${this.$store.getters["userType"]}/home`)
        }
        Vue.prototype.$connect(WS_URL, { format: 'json' });
      }
      console.log(Vue.prototype);
    }
  },
  sockets: {
    onopen() {
      let socket = Vue.prototype.$socket;
      const token = getLocalToken();
      socket.sendObj({type: 'auth', payload: token});
    },
    onmessage(event) {
      console.log(event);
      const obj = JSON.parse(event.data);
      console.log(obj);
    }
  },
  async beforeMount() {
    // this needs to be here so routing doesn't get messed up
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
