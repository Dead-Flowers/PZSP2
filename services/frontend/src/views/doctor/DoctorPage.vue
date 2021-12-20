<template>
  <div class="max-screen-space-container flex-row-items-start">
    <Navbar v-bind:usertype="'doctor'" />
    <div class="navbar-as-adjacent flex-column-items-centered">
      <ChangePassword />
    </div>
  </div>
</template>

<script>
import Navbar from '../../components/Navbar.vue'
import ChangePassword from '../../components/ChangePassword.vue'

export default {
  name: 'DoctorPage',
  components: {
    Navbar,
    ChangePassword,
  },
}
</script>

<style scoped>
</style>
