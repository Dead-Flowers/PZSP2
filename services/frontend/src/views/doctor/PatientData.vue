<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <Navbar v-bind:usertype="'doctor'" />
    <SearchUser v-if="!showSearchBox" v-bind:searchUser="searchUser" v-bind:userType="'patient'" />
    <div v-else>
      <PatientTable v-bind:patientData="patientData"/>
      <AnalysisResultTable v-bind:analyses="analyses" />
    </div>
  </div>
</template>

<script>
import Navbar from '../../components/Navbar.vue'
import SearchUser from '../../components/SearchUser.vue'
import PatientTable from '../../components/PatientTable.vue'
import AnalysisResultTable from '../../components/AnalysisResultTable.vue'

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
    searchUser(userId) {
      this.getUserData(userId);
      this.showSearchBox = true;
    },
    getUserData(id) {
      // TODO: this is a mock, we need to get data from backend 
      id = 11111;
      this.patientData = {
        patientId: id,
        firstName:"Bonifacy",
        secondName: "Rupert",
        surname: "Gąska",
        lastLab: "10-11-2021"
      }
      this.analyses = [{
          analysisId: 5,
          patientId: 11111,
          patientIdType: 'pesel',
          patientName: "Bonifacy Rupert",
          patientSurname: "Gąska",
          date: "02-01-2020",
          analysisHyperlink: "https://www.w3schools.com"
        },
        {
          analysisId: 4,
          patientId: 11111,
          patientIdType: 'pesel',
          patientName: "Bonifacy Rupert",
          patientSurname: "Gąska",
          date: "02-01-2020",
          analysisHyperlink: "https://www.w3schools.com"
        },
        {
          analysisId: 3,
          patientId: 11111,
          patientIdType: 'pesel',
          patientName: "Bonifacy Rupert",
          patientSurname: "Gąska",
          date: "02-01-2020",
          analysisHyperlink: "https://www.w3schools.com"
        },
        {
          analysisId: 2,
          patientId: 11111,
          patientIdType: 'pesel',
          patientName: "Bonifacy Rupert",
          patientSurname: "Gąska",
          date: "02-01-2020",
          analysisHyperlink: "https://www.w3schools.com"
        },
        {
          analysisId: 1,
          patientId: 11111,
          patientIdType: 'pesel',
          patientName: "Bonifacy Rupert",
          patientSurname: "Gąska",
          date: "02-01-2020",
          analysisHyperlink: "https://www.w3schools.com"
        },
      ]
    },
  },
}
</script>

<style>

</style>
