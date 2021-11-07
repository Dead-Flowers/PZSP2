<template>
  <div id="home">
    <Navbar />
    <div class="container">
    <AnalysisResultTable v-bind:analysisData="analysisData" />
    </div>
  </div>
</template>

<script>
import AnalysisResultTable from '../components/AnalysisResultTable.vue'
import Navbar from '../components/Navbar.vue'


export default {
  name: 'Home',
  components: {
  AnalysisResultTable,
  Navbar,
  },
  data() {
    // change the code of this method to get data from backend

    // this is a mock to test UI
    return {
      analysisData: [
        {
          analysisId: 1,
          patientId: 1,
          patientIdType: 'pesel',
          patientName: "Robert",
          patientSurname: "Kowalski",
          date: "02-01-2020",
          analysisHyperlink: "google.com"
        },
        {
          analysisId: 2,
          patientId: 1,
          patientIdType: 'pesel',
          patientName: "Robert",
          patientSurname: "Kowalski",
          date: "02-01-2020",
          analysisHyperlink: "google.com"
        },
        {
          analysisId: 3,
          patientId: "242rr32e32e24",
          patientIdType: 'passportNumber',
          patientName: "Andrzej",
          patientSurname: "Nowicki",
          date: "02-01-2020",
          analysisHyperlink: "google.com"
        },
        {
          analysisId: 4,
          patientId: 3,
          patientIdType: 'pesel',
          patientName: "Daniel",
          patientSurname: "Darko",
          date: "02-01-2020",
          analysisHyperlink: "google.com"
        },
        {
          analysisId: 5,
          patientId: 4,
          patientIdType: 'pesel',
          patientName: "Hubert",
          patientSurname: "Oklejka",
          date: "02-01-2020",
          analysisHyperlink: "google.com"
        },
      ]
    }
  }
}
</script>

<style>
#home {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
</style>
