<template>
  <div id="patient-data">
    <Navbar />
    <SearchPatient v-if="!showSearchBox" v-bind:searchPatient="searchPatient"/>
    <PatientTable v-else v-bind:patientData="patientData"/>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue'
import SearchPatient from '../components/SearchPatient.vue'
import PatientTable from '../components/PatientTable.vue'

export default {
  name: 'PatientData',
  components: {
    Navbar,
    SearchPatient,
    PatientTable
  },
  data() {
    return {
      showSearchBox: false,
      patientData: {}
    }
  },
  methods: {
    searchPatient(patientId) {
      this.getPatientData(patientId);
      this.showSearchBox = true;
    },
    getPatientData(id) {
      // TODO: this mock is a mock we need to get data from backend 
      this.patientData = {
        patientId: id,
        firstName:"Bonifacy",
        secondName: "Rupert",
        surname: "Gąska",
        lastLab: "10-11-2021"
      }
    },
  },
}
</script>

<style>
#patient-data {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
</style>
