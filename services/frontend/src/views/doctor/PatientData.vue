<template>
  <div class="max-screen-space-container flex-row-items-start">
    <Navbar v-bind:usertype="'doctor'" />
    <div class="navbar-as-adjacent flex-column-items-centered">
      <div class="sector">
        <SearchUser v-if="showSearchBox" v-bind:searchUser="searchUser" v-bind:userType="'patient'" />
        <div v-else>
          <PatientTable v-bind:patientData="patientData"/>
          <AnalysisResultTable v-bind:analysis="analyses" />
        </div>
      </div>
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
        const responeUser = await api.getUser(this.$store.getters["token"], id)
        this.patientData = responeUser.data
      } catch (e) {
        this.$store.dispatch("actionCheckApiError", e);
        this.$store.commit("openSnackbar", "Problem with getting patient data");
      }
      // pobiearz analizy
      try {
        const responeAnal = await api.getAnalysis(this.$store.getters["token"], id)
        this.analyses = responeAnal.data
      } catch (e) {
        this.$store.dispatch("actionCheckApiError", e);
        this.$store.commit("openSnackbar", "Problem with getting Analysis data");
      }
    },
  },
}
</script>

<style>

</style>
