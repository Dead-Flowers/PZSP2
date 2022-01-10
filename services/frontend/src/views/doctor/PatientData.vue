<template>
  <div>
    <SearchUser v-if="showSearchBox" v-bind:searchUser="searchUser" v-bind:userType="'patient'" />
    <div v-else>
      <PatientTable v-bind:patientData="patientData"/>
      <AnalysisResultTable v-bind:analyses="analyses" />
    </div>
  </div>
</template>

<script>
import SearchUser from '../../components/SearchUser.vue'
import PatientTable from '../../components/PatientTable.vue'
import AnalysisResultTable from '../../components/AnalysisResultTable.vue'
import { api } from '@/api';

export default {
  name: 'PatientData',
  components: {
    SearchUser,
    PatientTable,
    AnalysisResultTable
  },
  data() {
    return {
      showSearchBox: true,
      patientData: {},
      analyses: []
    }
  },
  methods: {
    async searchUser(user) {
      await this.getUserData(user.id);
      this.showSearchBox = false;
    },
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
      const obj = JSON.parse(event.data);
      if (obj.type != "analysis-state-updated") return;
      for (let analysis of this.analyses) {
        if (analysis.id != obj.payload.id) continue;
        analysis.status = obj.payload.status;
        console.log('updated analysis status');
        return;
      }
      console.log("analysis not found, refetching");
      //const analyses = await api.getAnalysis(this.$store.getters["token"], id)
      //this.analyses = analyses.data
    }
  }
}
</script>

<style>

</style>
