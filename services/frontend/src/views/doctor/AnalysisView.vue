<template>
  <div>
    <AnalysisVisualization v-if="analisyFinished" v-bind:analysisData="analysisData" v-bind:patient="patient"/>
    <div v-else>
        <v-row>
          <v-progress-circular
          :size="200"
          :width="20"
          color="purple"
          indeterminate
          ></v-progress-circular>
          <div>Analiza nie została jeszcze zakończona</div>
        </v-row>
    </div>
  </div>
</template>

<script>
import AnalysisVisualization from '../../components/AnalysisVisualization.vue'
import { api } from '@/api';

export default {
  name: 'AnalysisView',
  components: {
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
      this.loading = true
      // get status and patient id
      let response = await api.getAnalysisResults(this.$store.getters["token"], this.$route.params.id)
      if (response.data.status != "COMPLETED") {
        this.$store.commit("openSnackbar", "Analisysy not finished yet");
        return;
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
      this.analisyFinished = true;
      this.loading = false;
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
