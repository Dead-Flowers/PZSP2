<template>
    <div>
      <AnalysisVisualization v-if="!loading" v-bind:analysisData="analysisData" v-bind:patient="patient"/>
      <div v-else>
          <v-row>
            <v-progress-circular
            :size="200"
            :width="20"
            color="purple"
            indeterminate
            ></v-progress-circular>
            <div>Trwa ładowanie...</div>
          </v-row>
      </div>
    </div>
</template>

<script>
import AnalysisVisualization from '../../components/AnalysisVisualization.vue'
import { api } from '@/api';

const dummy_patient = {
  patientIdType: 'pesel',
  pesel: "...",
  first_name: "...",
  second_name: "...",
  last_name: "...",
};

export default {
  name: 'AnalysisView',
  components: {
    AnalysisVisualization,
  },
  data() {
    return {
      analysisStatus: null,
      analysisData: [],
      patient: dummy_patient,
      patientLoaded: false
    }
  },
  computed: {
    loading() {
      return this.analysisStatus != "COMPLETED" || !this.patientLoaded;
    },
    analysisId() {
      return this.$route.params.id;
    }
  },
  async mounted() {
    await this.updateAnalysis();
  },
  methods: {
    async updateAnalysis() {
      try 
      {
        const analysis = await api.getAnalysisResults(this.$store.getters["token"], this.analysisId)
        this.analysisStatus = analysis.data.status;
        if (!this.patientLoaded) {
          const patient = await api.getUser(this.$store.getters["token"], analysis.data.patient_id)
          this.patient = patient.data;
          this.patientLoaded = true;
        }
        if (analysis.data.status != "COMPLETED") {
          this.$store.commit("openSnackbar", `Analysis status: ${analysis.data.status}`);
          return;
        }

        // get frames 
        let data = []
        const frames = await api.getFrames(this.$store.getters["token"], this.analysisId)
        for(const element of frames.data)
        {
          data.push(element.probability)
        }
        this.analysisData = data
      } catch (error) {
          console.log(error)
          this.$store.dispatch("actionCheckApiError", error);
          this.$store.commit("openSnackbar", "Problem with getting analysis results");
      }
    }
  },
  sockets: {
    onmessage(event) {
      const obj = JSON.parse(event.data);
      console.log(obj);
      if (obj.type == "analysis-state-updated") {
        if (obj.payload.id == this.analysisId) {
          this.updateAnalysis();
        }
      }
    }
  }
}
</script>

<style>

.analysisVisualization {
  width: 60%
}

</style>
