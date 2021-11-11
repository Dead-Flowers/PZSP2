<template>
  <form class="flex-column-items-start">
    <input
      class="input-element-standard"
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
