<template>
  <div id="login">
    <SignIn />
  </div>
</template>

<script>
import SignIn from '../components/SignIn.vue'


export default {
  name: 'Login',
  components: {
  SignIn
  }
}
</script>

<style>
#login {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
</style>
