<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <Navbar v-bind:usertype="'doctor'" />
    <label>Witaj {{username}}!</label>
  </div>
</template>

<script>
import Navbar from '../../components/Navbar.vue'

export default {
  name: 'DoctorPage',
  components: {
    Navbar,
  },
  data() {
    return {
      username: 'Test',
    }
  },

}
</script>

<style scoped>
label {
  font-size: 4rem;
}
</style>
