<template>
  <div>
    Analiza została uruchomiona
    <v-btn @click="goToAnalisy">
        Wyniki analizy 
    </v-btn>
  </div>
</template>

<script>
import router from '../../router'
export default {
  name: "AnalysisStarted",
  methods: {
      goToAnalisy(){
          router.push(`/doctor/analysis/${this.$store.getters["getAnalysisID"]}`)
      }
  }
}
</script>

<style>

</style>