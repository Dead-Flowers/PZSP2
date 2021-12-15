<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <Navbar v-bind:pageType="'patient'" />
  </div>
</template>

<script>
import Navbar from '../../components/Navbar.vue'

export default {
  name: 'PatientPage',
  components: {
    Navbar,
  },
}
</script>

<style>
</style>
