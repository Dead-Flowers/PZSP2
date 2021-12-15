<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <Login v-bind:pageType="'admin'" />
  </div>
</template>

<script>
import Login from '../../components/Login.vue'


export default {
  name: 'AdminLogin',
  props: ["pageType"],
  components: {
  Login
  }
}
</script>

<style>

</style>
ś