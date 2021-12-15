<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <RegisterPatientForm />
  </div>
</template>

<script>
import RegisterPatientForm from '../../components/RegisterPatientForm.vue'

export default {
  name: 'NewPatient',
  components: {
    RegisterPatientForm
  },
}
</script>

<style>

</style>
