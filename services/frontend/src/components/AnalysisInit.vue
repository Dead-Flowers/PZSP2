<template>
  <v-form
    ref="form"
    v-model="analysis_file"
    @submit="(e) => { e.preventDefault(); startAnalysis(); }"
  >
    <v-btn
      :disabled="!analysis_file"
      color="success"
      class="mr-4"
      type="submit"
    >
      Rozpocznij analizę
    </v-btn>
    <v-file-input
      accept=".mp3,.wav, .raw, .mp4, .oog, .aac"
      label="Wybierz Plik"
      v-model="analysis_file"
    >
    </v-file-input>
  </v-form>
</template>

<script>
import router from '../router'
import { api } from '@/api';

export default {
  name: "AnalysisInit",
  props: ["patientID"],
  data() {
    return {
      analysis_file: [],
    }
  },
  methods: {
    async startAnalysis() {
      this.uploadFile(this.analysis_file, this.patientID);
      router.push('/doctor/analysisStarted');
      },
    async uploadFile (file, patientID) {
      try {
        let formData = new FormData();
        formData.append('file_in', file);
        let response = await api.uploadFile(this.$store.getters["token"], formData, patientID)
        let recordingID = response.data

        response = await api.startAnalysis(this.$store.getters["token"], recordingID)
        this.$store.commit("setAnalysisID", response.data)
      } catch (e) {
        await this.$store.dispatch("actionCheckApiError", e);
        this.$store.commit("openSnackbar", "Problem with uploading file!");
      }
    } 
  },
}
</script>

<style scoped>

</style>
