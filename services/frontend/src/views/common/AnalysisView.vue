<template>
    <div class="analysisVisualization" >
      <AnalysisVisualization v-if="!loading" v-bind:analysisData="analysisData" v-bind:patient="patient" v-bind:analysisStats="analysisStats" v-bind:recordingId="recordingId"/>
      <div v-else>
          <img src="https://i.imgur.com/0wii1FM.gif" />
          <div>Trwa ładowanie...</div>
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

const dummy_stats = {
    percent_of_bowel_sounds_followed_by_another_bowel_sound_within_100_ms: 0,
    percent_of_bowel_sounds_followed_by_another_bowel_sound_within_200_ms: 0,
    percent_of_bowel_sounds_followed_by_another_bowel_sound_within_50_ms: 0,
    bowel_sounds_identified_total_count: 0,
    bowel_sounds_per_minute_1st_decile: 0,
    bowel_sounds_per_minute_1st_quartile: 0,
    bowel_sounds_per_minute_3rd_quartile: 0,
    bowel_sounds_per_minute_9th_decile: 0,
    bowel_sounds_per_minute_maximum: 0,
    bowel_sounds_per_minute_mean: 0,
    bowel_sounds_per_minute_median: 0,
    bowel_sounds_per_minute_minimum: 0,
    bowel_sounds_per_minute_standard_deviation: 0,
    bowel_sounds_per_minute_total: 0,
    frequency_analysis_in_three_minute_periods: "",
    recording_length_hours_minutes_seconds: "0",
    recording_length_minutes: 0
}


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
      patientLoaded: false,
      recordingId: null,
      analysisStats: dummy_stats
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
        this.recordingId = analysis.data.recording_id;
        if (!this.patientLoaded) {
          const patient = await api.getUser(this.$store.getters["token"], analysis.data.patient_id)
          this.patient = patient.data;
          this.patientLoaded = true;
        }
        if (analysis.data.status != "COMPLETED") {
          this.$store.commit("openSnackbar", `Status analizy: ${analysis.data.status}`);
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


        //get statistics
        const stats = await api.getAnalysisStatistics(this.$store.getters["token"], this.analysisId)
        this.analysisStats = stats.data.main_results
      } catch (error) {
          this.$store.dispatch("actionCheckApiError", error);
          if (!this.$store.getters["isLoggedIn"]) {
            this.$router.push("/login");
          }
          this.$store.commit("openSnackbar", "Wystąpił błąd podczas pobierania wyników analizy");
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
  min-width: 70vw
}

</style>
