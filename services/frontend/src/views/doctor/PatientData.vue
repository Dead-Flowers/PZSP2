<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <Navbar v-bind:usertype="'doctor'" />
    <SearchUser v-if="!showSearchBox" v-bind:searchUser="searchUser" v-bind:userType="'patient'" />
    <div v-else>
      <PatientTable v-bind:patientData="patientData"/>
      <AnalysisResultTable v-bind:analysis="analyses" />
    </div>
  </div>
</template>

<script>
import Navbar from '../../components/Navbar.vue'
import SearchUser from '../../components/SearchUser.vue'
import PatientTable from '../../components/PatientTable.vue'
import AnalysisResultTable from '../../components/AnalysisResultTable.vue'
import { api } from '@/api';

export default {
  name: 'PatientData',
  components: {
    Navbar,
    SearchUser,
    PatientTable,
    AnalysisResultTable
  },
  data() {
    return {
      showSearchBox: false,
      patientData: {},
      analyses: []
    }
  },
  methods: {
    async searchUser(userId) {
      await this.getUserData(userId);
      this.showSearchBox = true;
    },
    async getUserData(id) {
      // TODO: this is a mock, we need to get data from backend 
      // pobierz dane pacjetna    
      //TODO: catch err  
      const responeUser = await api.getUser(this.$store.getters["token"], id)
      console.log(responeUser)
      this.patientData = responeUser.data
      console.log(this.patientData)
      // pobiearz analizy
      const responeAnal = await api.getAnalysis(this.$store.getters["token"], id)
      console.log(responeAnal)
      this.analyses = responeAnal.data
      console.log(this.analyses)
    },
  },
}
</script>

<style>

</style>
