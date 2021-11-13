<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <Navbar />
    <SearchPatient v-if="!showSearchBox" v-bind:searchPatient="searchPatient"/>
    <div v-else>
      <PatientTable v-bind:patientData="patientData"/>
      <AnalysisResultTable v-bind:analyses="analyses" />
    </div>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue'
import SearchPatient from '../components/SearchPatient.vue'
import PatientTable from '../components/PatientTable.vue'
import AnalysisResultTable from '../components/AnalysisResultTable.vue'

export default {
  name: 'PatientData',
  components: {
    Navbar,
    SearchPatient,
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
    searchPatient(patientId) {
      this.getPatientData(patientId);
      this.showSearchBox = true;
    },
    getPatientData(id) {
      // TODO: this is a mock, we need to get data from backend 
      this.patientData = {
        patientId: id,
        firstName:"Bonifacy",
        secondName: "Rupert",
        surname: "Gąska",
        lastLab: "10-11-2021"
      }
      this.analyses = [{
          analysisId: 1,
          patientId: 1,
          patientIdType: 'pesel',
          patientName: "Bonifacy Rupert",
          patientSurname: "Gąska",
          date: "02-01-2020",
          analysisHyperlink: "https://www.google.com"
        },
        {
          analysisId: 2,
          patientId: 1,
          patientIdType: 'pesel',
          patientName: "Bonifacy Rupert",
          patientSurname: "Gąska",
          date: "02-01-2020",
          analysisHyperlink: "https://www.google.com"
        },
        {
          analysisId: 3,
          patientId: 1,
          patientIdType: 'pesel',
          patientName: "Bonifacy Rupert",
          patientSurname: "Gąska",
          date: "02-01-2020",
          analysisHyperlink: "https://www.google.com"
        },
        {
          analysisId: 4,
          patientId: 1,
          patientIdType: 'pesel',
          patientName: "Bonifacy Rupert",
          patientSurname: "Gąska",
          date: "02-01-2020",
          analysisHyperlink: "https://www.google.com"
        },
        {
          analysisId: 5,
          patientId: 1,
          patientIdType: 'pesel',
          patientName: "Bonifacy Rupert",
          patientSurname: "Gąska",
          date: "02-01-2020",
          analysisHyperlink: "https://www.google.com"
        },
      ]
    },
  },
}
</script>

<style>

</style>
