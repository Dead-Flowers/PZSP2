<template>
  <form class="login-box sector flex-column-items-centered">
    Witaj, zaloguj się
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="login"
      placeholder="Login..."
      v-model="username"
      autocomplete="off"
    />
    <input
      class="input-element-standard keyboard-input"
      type="password"
      name="password"
      placeholder="Hasło..."
      v-model="password"
      autocomplete="off"
    />
    <a  
      class="input-element-standard button link"
      href="https://www.w3schools.com"
    >
      Zapomniałeś hasła?
    </a>
    <input
      class="input-element-standard button"
      type="button"
      value="Zaloguj się"
      @click="checkLogin"
    />
    <router-link to="/" class="go-home" > Powróć do strony głównej </router-link>
  </form>
</template>

<script>
import router from '../router'

export default {
  name: 'Login',
  data() {
    return {
      username: null,
      password: null
    }
  },
  methods: {
    async checkLogin() {
      let payload = {
        username: this.username,
        password: this.password,
      }
      await this.$store.dispatch("actionLogIn", payload);
      
      if (this.$store.getters["isLoggedIn"]) {
        this.acceptLogin();
      }
      else {
        this.rejectLogin();
      }
    },
    acceptLogin() {
      console.log('Logowanie powiodło się');
      router.push(`/${this.$store.getters["userType"]}/home`)
    },
    rejectLogin() {
      this.username=null;
      this.password=null;
      console.log('Logowanie nie powiodło się');
      alert("Niepoprawny login");
    }
  }
}
</script>

<style scoped>
.login-box {
  padding-block: 2vw;
  padding-inline: 2.5vw;
  font-size: 2vw;
}
</style>