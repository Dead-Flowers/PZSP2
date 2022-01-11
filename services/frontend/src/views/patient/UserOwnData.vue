<template>
  <div>
    <PatientData v-bind:patientId="this.$store.getters['id']" />
  </div>
</template>

<script>
import PatientData from '../../components/PatientData.vue'

export default {
  name: "UserOwnData",
  components: {
    PatientData,
  },
  
};
</script>

<style>
</style>