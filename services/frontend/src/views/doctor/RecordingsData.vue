<template>
  <div>
    <PatientTable v-bind:patientData="patientData"/>
    <RecordingsTable v-bind:recordings="recordings" />
  </div>
</template>

<script>
import PatientTable from '../../components/PatientTable.vue'
import RecordingsTable from '../../components/RecordingsTable.vue'
import { api } from '@/api';

export default {
  name: 'PatientData',
  components: {
    PatientTable,
    RecordingsTable
  },
  data() {
    return {
      patientData: {},
      recordings: []
    }
  },
  methods: {
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
  beforeMount() {
    this.getUserData(this.$route.params.id)
  }
}
</script>

<style>

</style>