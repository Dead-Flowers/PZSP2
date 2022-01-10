<template>
  <div>
    <div>
      Analiza została uruchomiona
    </div>
    <div>
      <v-btn @click="goToAnalysis">
          Wyniki analizy 
      </v-btn>
    </div>
  </div>
</template>

<script>
import router from '../../router'
export default {
  name: "AnalysisStarted",
  methods: {
      goToAnalysis(){
          router.push(`/doctor/analysis/${this.$route.params.id}`)
      }
  }
}
</script>

<style>

</style>