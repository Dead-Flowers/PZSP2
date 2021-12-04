<template>
  <form class="sector flex-column-items-start">
    <input
      class="input-element-standard"
      style="margin-block-start: 0px"
      type="button"
      value="Rozpocznij Analizę"
      :disabled="noFiles"
      @click="startAnalysis"
    />
    <input
      class="input-file-field"
      type="file"
      name="bowel-sound-file"
      accept=".mp3"
      @change="fileChange"
    />
  </form>
</template>

<script>
import router from '../router'

export default {
  name: "AnalysisInit",
  data() {
    return {
      noFiles: true,
    }
  },
  methods: {
    startAnalysis() {
      this.$store.dispatch("uploadFile");
      this.$store.dispatch("startAnalysis");
      router.push('analysis-view');
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
