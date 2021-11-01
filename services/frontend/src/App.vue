<template>
  <div id="app">
    <AnalysisInit />
    <AnalysisResultTable v-bind:analysisData="analysisData" />
    <Navbar />
    <PatientTable />
    <RegisterPatient />
    <SearchPatient />
    <SignIn />
    <SignUp />
  </div>
</template>

<script>
//import AnalysisInit from './components/AnalysisInit.vue'
import AnalysisResultTable from './components/AnalysisResultTable.vue'
//import Navbar from './components/Navbar.vue'
//import PatientTable from './components/PatientTable.vue'
//import RegisterPatient from './components/RegisterPatient.vue'
//import SearchPatient from './components/SearchPatient.vue'
//import SignIn from './components/SignIn.vue'
//import SignUp from './components/SignUp.vue'


export default {
  name: 'App',
  components: {
  //AnalysisInit,
  AnalysisResultTable,
  //Navbar,
  //PatientTable,
  //RegisterPatient,
  //SearchPatient,
  //SignIn,
  //SignUp,
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
#app {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
</style>
