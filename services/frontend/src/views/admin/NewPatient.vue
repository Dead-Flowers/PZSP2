<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <Navbar v-bind:usertype="'admin'" />
    <RegisterPatientForm />
  </div>
</template>

<script>
import RegisterPatientForm from '../../components/RegisterPatientForm.vue'
import Navbar from '../../components/Navbar.vue'

export default {
  name: 'NewPatient',
  components: {
    Navbar,
    RegisterPatientForm,
  },
}
</script>

<style>

</style>
