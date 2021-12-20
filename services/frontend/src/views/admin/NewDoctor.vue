<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <Navbar v-bind:usertype="'admin'" />
    <RegisterUserForm v-bind:usertype="'doctor'" />
  </div>
</template>

<script>
import RegisterUserForm from '../../components/RegisterUserForm.vue'
import Navbar from '../../components/Navbar.vue'

export default {
  name: 'NewDoctor',
  components: {
    Navbar,
    RegisterUserForm,
  },
}
</script>

<style>

</style>
