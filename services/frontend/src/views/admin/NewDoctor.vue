<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <RegisterDoctorForm />
  </div>
</template>

<script>
import RegisterDoctorForm from '../../components/RegisterDoctorForm.vue'

export default {
  name: 'NewDoctor',
  components: {
    RegisterDoctorForm
  },
}
</script>

<style>

</style>
