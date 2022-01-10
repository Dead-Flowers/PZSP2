<template>
  <v-form
    ref="form"
    v-model="valid"
    @submit="(e) => {e.preventDefault(); checkLogin();}"
  >
    <h1>Witaj, zaloguj się</h1>
    <v-text-field
      v-model="email"
      :rules="emailRules"
      label="E-mail"
    />
    <v-text-field
      v-model="password"
      :rules="passwordRules"
      type="password"
      label="Hasło"
    />


    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      type="submit"
    >
      Zaloguj się
    </v-btn>
    <!--
    <v-btn
      color="error"
      class="mr-4"
      @click="forgotPassword"
    >
      Zapomniałeś hasła?
    </v-btn>
    -->
    <v-btn
      color="warning"
      @click="goToFrontpage"
    >
      Powróć do strony głównej
    </v-btn>
  </v-form>
</template>

<script>
import router from '../router'

export default {
  name: 'Login',
  data() {
    return {
      email: null,
      password: null,
      emailRules: [
        v => !!v || 'E-mail jest wymagany',
        v => /.+@.+\..+/.test(v) || 'E-mail musi być poprawny',
      ],
      passwordRules: [
        v => !!v || 'Hasło jest wymagane',
      ],
      valid: false,
    }
  },
  methods: {
    async checkLogin() {
      let payload = {
        username: this.email,
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
      this.email=null;
      this.password=null;
      console.log('Logowanie nie powiodło się');
      alert("Niepoprawny login");
    },
    goToFrontpage (){
      router.push("/");
    },
    forgotPassword () {
      //TODO
      alert("Ta funkcja jeszcze nie istnieje");
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