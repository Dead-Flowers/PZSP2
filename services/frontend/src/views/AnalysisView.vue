<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <Navbar />
    <AnalysisVisualization v-bind:analysisData="analysisData"/>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue'
import AnalysisVisualization from '../components/AnalysisVisualization.vue'

export default {
  name: 'AnalysisView',
  components: {
    Navbar,
    AnalysisVisualization,
  },
  data() {
    return {
      // this is a mock
      analysisData: {
        graphData: [
          
        ]
      }
    }
  }
}
</script>

<style>

</style>
