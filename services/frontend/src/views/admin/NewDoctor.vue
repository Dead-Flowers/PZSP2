<template>
  <div class="max-screen-space-container flex-row-items-start">
    <Navbar v-bind:usertype="'admin'" />
    <div class="navbar-as-adjacent flex-column-items-centered">
      <RegisterUserForm v-bind:usertype="'doctor'" />
    </div>
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
