<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <Navbar v-bind:pageType="'admin'" />
  </div>
</template>

<script>
import Navbar from '../../components/Navbar.vue'

export default {
  name: 'AdminPage',
  components: {
    Navbar,
  },
}
</script>

<style>
</style>
