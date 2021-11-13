<template>
  <form class="sector flex-column-items-start">
    <input
      class="input-element-standard"
      style="margin-block-start: 0px"
      type="button"
      value="Rozpocznij Analizę"
    />
    <input
      class="input-file-field"
      type="file"
      name="bowel-sound-file"
      accept=".mp3"
    />
  </form>
</template>

<script>

export default {
  name: "AnalysisInit"
}
</script>

<style scoped>

</style>
