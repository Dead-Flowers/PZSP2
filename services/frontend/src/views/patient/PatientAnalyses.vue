<template>
  <div class="max-screen-space-container flex-row-items-start">
    <Navbar v-bind:usertype="'doctor'" />
    <div class="navbar-as-adjacent flex-column-items-centered">
      <div class="sector">
        <PatientTable v-bind:patientData="patientData"/>
        <AnalysisResultTable v-bind:analyses="analyses" />
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from '../../components/Navbar.vue'
import PatientTable from '../../components/PatientTable.vue'
import AnalysisResultTable from '../../components/AnalysisResultTable.vue'
import { api } from '@/api';

export default {
  name: 'PatientData',
  components: {
    Navbar,
    PatientTable,
    AnalysisResultTable
  },
  data() {
    return {
      showSearchBox: true,
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