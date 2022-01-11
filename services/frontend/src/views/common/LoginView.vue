<template>
    <LoginForm/>
</template>

<script>
import LoginForm from '../../components/LoginForm.vue'
import router from '../../router';


export default {
  name: 'Login',
  components: {
  LoginForm
  },
  beforeMount() {
    if (this.$store.getters["isLoggedIn"]) {
      router.push(`/${this.$store.getters["userType"]}/home`);
    }
    else {
      router.push("/");
    }
  },
}
</script>

<style>

</style>
