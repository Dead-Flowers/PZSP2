<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <Navbar v-bind:usertype="'patient'" />
    <ChangePassword />
  </div>
</template>

<script>
import Navbar from '../../components/Navbar.vue'
import ChangePassword from '../../components/ChangePassword.vue'

export default {
  name: 'PatientPage',
  components: {
    Navbar,
    ChangePassword,
  },
}
</script>

<style>
</style>
