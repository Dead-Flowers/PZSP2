<template>
  <v-form
    ref="form"
    @submit="
      (e) => {
        e.preventDefault();
        startAnalysis();
      }
    "
  >
    <v-btn
      :disabled="!analysis_file || analysis_file.length == 0"
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
import { api } from "@/api";
import router from "../router";

export default {
  name: "AnalysisInit",
  props: ["patientID"],
  data() {
    return {
      analysis_file: [],
    };
  },
  methods: {
    async startAnalysis() {
      let analysis_id = await this.uploadFile(
        this.analysis_file,
        this.patientID
      );
      router.push(`/doctor/analysisStarted/${analysis_id}`);
    },
    async uploadFile(file, patientID) {
      try {
        let formData = new FormData();
        formData.append("file_in", file);
        let response = await api.uploadFile(
          this.$store.getters["token"],
          formData,
          patientID
        );
        let recordingID = response.data;

        response = await api.startAnalysis(
          this.$store.getters["token"],
          recordingID
        );
        return response.data;
      } catch (e) {
        await this.$store.dispatch("actionCheckApiError", e);
        this.$store.commit(
          "openSnackbar",
          "Wystąpił problem podczas wysyłania nagrania"
        );
      }
    },
  },
};
</script>

<style scoped>
</style>
