<template>
  <div class="max-screen-space-container flex-row-items-start">
    <Navbar v-bind:usertype="'doctor'" />
    <div class="navbar-as-adjacent flex-column-items-centered">
      <AnalysisVisualization v-bind:analysisData="analysisData" v-bind:patient="patient"/>
    </div>
  </div>
</template>

<script>
import Navbar from '../../components/Navbar.vue'
import AnalysisVisualization from '../../components/AnalysisVisualization.vue'
import { api } from '@/api';

export default {
  name: 'AnalysisView',
  components: {
    Navbar,
    AnalysisVisualization,
  },
  data() {
    return {
      loading: true,
      analisyFinished: false,
      analysisData: [],
      patient: {
        patientIdType: 'pesel',
        pesel: "0123456789",
        first_name: "wait for fetch",
        second_name: "wait for fetch",
        last_name: "wait fo fetch",
      }
    }
  },
  async mounted() {
    try {
      // get status and patient id
      let response = await api.getAnalysisResults(this.$store.getters["token"], this.$route.params.id)
      if (response.data.status != "COMPLETED") {
        this.$store.commit("openSnackbar", "Analisysy not finished yet");
      }
      // get patient data
      response = await api.getUser(this.$store.getters["token"], response.data.patient_id)
      this.patient = response.data
      // get frames 
      let data = []
      response = await api.getFrames(this.$store.getters["token"], this.$route.params.id)
      for(const element of response.data)
      {
        data.push(element.probability)
      }
      this.analysisData = data
    }  catch (error) {
        console.log(error)
        this.$store.dispatch("actionCheckApiError", error);
        this.$store.commit("openSnackbar", "Problem with getting analisy results");
    }
  }
}
</script>

<style>

</style>
