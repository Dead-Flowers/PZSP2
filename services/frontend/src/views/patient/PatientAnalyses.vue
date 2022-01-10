<template>
  <div>
    <PatientTable v-bind:patientData="patientData"/>
    <AnalysisResultTable v-bind:analyses="analyses" />
  </div>
</template>

<script>
import PatientTable from '../../components/PatientTable.vue'
import AnalysisResultTable from '../../components/AnalysisResultTable.vue'
import { api } from '@/api';

export default {
  name: 'PatientData',
  components: {
    PatientTable,
    AnalysisResultTable
  },
  data() {
    return {
      loading: true,
      patientData: {},
      analyses: []
    }
  },
  async mounted() {
      // pobierz dane pacjetna
      try {
        const responeUser = await api.getUser(this.$store.getters["token"], this.$store.getters["id"])
        this.patientData = responeUser.data
      } catch (e) {
        this.$store.dispatch("actionCheckApiError", e);
        this.$store.commit("openSnackbar", "Problem with getting patient data");
      }
      // pobiearz analizy
      try {
        const responeAnal = await api.getAnalysis(this.$store.getters["token"], this.$store.getters["id"])
        this.analyses = responeAnal.data
      } catch (e) {
        this.$store.dispatch("actionCheckApiError", e);
        this.$store.commit("openSnackbar", "Problem with getting Analysis data");
      }
  },
}
</script>

<style>

</style>