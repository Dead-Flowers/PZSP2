<template>
  <form class="sector flex-column-items-centered">
    <label >Witaj {{username}}!</label>
    <label>Logujesz się po raz pierwszy. Ustaw hasło.</label>
    <input
    class="input-element-standard keyboard-input"
    type="password"
    name="password"
    placeholder="Hasło..."
    v-model="password"
    autocomplete="off"
    />
    <input
      class="input-element-standard keyboard-input"
      type="password"
      name="password-confirm"
      placeholder="Powtórz Hasło..."
      v-model="confirmPassword"
      autocomplete="off"
    />
    <input
      class="input-element-standard button"
      type="button"
      value="Ustaw"
      @click="setPasswd"
    />
  </form>
</template>

<script>
import router from '../router'

export default {
  name: 'SetupPasswd',
  props: ['usertype'],
  data() {
    return {
      username: null,
      password: null,
      confirmPassword: null,
    }
  },
  methods: {
    setPasswd: function () {
      // password validation(8characters, big letter, small letter, number, special char) etc
      console.log('Setup password', this.password);
      router.push(`/${this.usertype}/home`);
    },
    getUserId: function () {
      this.username = this.$route.query.userId;
    },
  },
  beforeMount() {
    this.getUserId();
  }
}
</script>

<style scoped>
label {
  margin-block-end: 10px;
}

</style>