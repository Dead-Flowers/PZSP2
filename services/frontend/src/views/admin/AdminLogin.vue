<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <Login v-bind:usertype="'admin'" />
  </div>
</template>

<script>
import Login from '../../components/Login.vue'
export default {
  name: 'AdminLogin',
  props: ["usertype"],
  components: {
  Login
  }
}
</script>

<style>
</style>