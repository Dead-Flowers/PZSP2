<template>
  <div>
    <PatientData v-bind:patientId="this.$route.params.id" />
  </div>
</template>

<script>
import PatientData from '../../components/PatientData.vue'

export default {
  name: "PatientAnalyses",
  components: {
    PatientData,
  },
  
};
</script>

<style>
</style>