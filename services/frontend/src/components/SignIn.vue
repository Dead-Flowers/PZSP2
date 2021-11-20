<template>
  <form class="sign-in-box sector flex-column-items-centered">
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
      href="https://www.google.com"
    >
      Zapomniałeś hasła?
    </a>
    <div >
      <input
        class="input-element-standard button"
        type="button"
        value="Zaloguj się"
        style="margin-inline-end: 20px"
        @click="checkLogin"
      />
      <input
        class="input-element-standard button"
        type="button"
        value="Załóż konto"
      />
    </div>
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
    checkLogin() {
      // TODO: this is a mock
      if (this.username == "test" && this.password == "test") {
        this.acceptLogin();
      }
      else {
        this.rejectLogin();
      }
    },
    acceptLogin() {
      console.log('Logowanie powiodło się');
      router.push('home')
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
.sign-in-box {
  padding-block: 40px;
  padding-inline: 50px;
  font-size: 2rem;
}
</style>