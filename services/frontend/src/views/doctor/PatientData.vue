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
      patientData: {},
      analyses: []
    }
  },
  methods: {
    async getUserData(id) {
      // pobierz dane pacjetna    
      try {
        const patient = await api.getUser(this.$store.getters["token"], id)
        this.patientData = patient.data
      } catch (e) {
        this.$store.dispatch("actionCheckApiError", e);
        this.$store.commit("openSnackbar", "Problem with getting patient data");
      }
      // pobiearz analizy
      try {
        const analyses = await api.getAnalysis(this.$store.getters["token"], id)
        this.analyses = analyses.data
        console.log(analyses);
      } catch (e) {
        this.$store.dispatch("actionCheckApiError", e);
        this.$store.commit("openSnackbar", "Problem with getting Analysis data");
      }
    },
  },
  sockets: {
    onmessage(event) {
      // listen for changes and update existing analyses
      // if such an analysis doesn't exist, refetch all
      const obj = JSON.parse(event.data);
      if (obj.type != "analysis-state-updated") return;
      for (let analysis of this.analyses) {
        if (analysis.id != obj.payload.id) continue;
        analysis.status = obj.payload.status;
        console.log('updated analysis status');
        return;
      }
      console.log("analysis not found, refetching");
      // TODO: REFETCH ALL ANALYSES HERE 
      //const analyses = await api.getAnalysis(this.$store.getters["token"], id)
      //this.analyses = analyses.data
    }
  },
  beforeMount() {
    this.getUserData(this.$route.params.id)
  }
}
</script>

<style>

</style>
