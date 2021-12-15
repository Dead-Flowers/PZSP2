<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <Login v-bind:pageType="'doctor'" />
  </div>
</template>

<script>
import Login from '../../components/Login.vue'


export default {
  name: 'DoctorLogin',
  props: ["pageType"],
  components: {
  Login
  }
}
</script>

<style>

</style>
ś