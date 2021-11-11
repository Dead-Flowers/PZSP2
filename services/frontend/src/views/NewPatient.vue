<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <RegisterPatient />
  </div>
</template>

<script>
import RegisterPatient from '../components/RegisterPatient.vue'

export default {
  name: 'NewPatient',
  components: {
    RegisterPatient
  },
}
</script>

<style>

</style>
