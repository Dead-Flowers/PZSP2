<template>
  <div class="max-screen-space-container flex-row-items-start">
    <div class="navbar-as-adjacent flex-column-items-centered">
      <ChangePassword />
    </div>
  </div>
</template>

<script>
import ChangePassword from '../../components/ChangePassword.vue'

export default {
  name: 'PatientPage',
  components: {
    ChangePassword,
  },
}
</script>

<style>
</style>
