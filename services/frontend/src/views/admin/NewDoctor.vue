<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <Navbar v-bind:usertype="'admin'" />
    <RegisterDoctorForm />
  </div>
</template>

<script>
import RegisterDoctorForm from '../../components/RegisterDoctorForm.vue'
import Navbar from '../../components/Navbar.vue'

export default {
  name: 'NewDoctor',
  components: {
    Navbar,
    RegisterDoctorForm,
  },
}
</script>

<style>

</style>
