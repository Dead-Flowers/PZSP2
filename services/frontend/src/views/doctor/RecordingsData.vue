<template>
  <div class="max-screen-space-container flex-row-items-start">
    <div class="navbar-as-adjacent flex-column-items-centered">
      <div class="sector">
        <SearchUser v-if="showSearchBox" v-bind:searchUser="searchUser" v-bind:userType="'patient'" />
        <div v-else>
          <PatientTable v-bind:patientData="patientData"/>
          <RecordingsTable v-bind:recordings="recordings" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SearchUser from '../../components/SearchUser.vue'
import PatientTable from '../../components/PatientTable.vue'
import RecordingsTable from '../../components/RecordingsTable.vue'
import { api } from '@/api';

export default {
  name: 'PatientData',
  components: {
    SearchUser,
    PatientTable,
    RecordingsTable
  },
  data() {
    return {
      showSearchBox: true,
      patientData: {},
      recordings: []
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
        const responeRec = await api.getRecordings(this.$store.getters["token"], id)
        this.recordings = responeRec.data
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