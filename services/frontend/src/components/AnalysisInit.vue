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
      @change="fileChange"
    >
    </v-file-input>
  </v-form>
</template>

<script>
import router from '../router'

export default {
  name: "AnalysisInit",
  props: ["patientID"],
  data() {
    return {
      analysis_file: null,
    }
  },
  methods: {
    async startAnalysis() {
      await this.$store.dispatch("uploadFile", { patientID: this.patientID});
      router.push('/doctor/analysis-view');
    },
    fileChange(event) {
      this.noFiles = !event.target.files.length;
      if (!this.noFiles) {
        this.$store.commit("setAnalysisFile", event.target.files[0])
      }
    }
  }
}
</script>

<style scoped>

</style>
