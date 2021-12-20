<template>
  <div class="max-screen-space-container flex-row-items-start">
    <Navbar v-bind:usertype="'doctor'" />
    <div class="navbar-as-adjacent flex-column-items-centered">
      <AnalysisVisualization v-bind:analysisData="analysisData"/>
    </div>
  </div>
</template>

<script>
import Navbar from '../../components/Navbar.vue'
import AnalysisVisualization from '../../components/AnalysisVisualization.vue'

export default {
  name: 'AnalysisView',
  components: {
    Navbar,
    AnalysisVisualization,
  },
  data() {
    return {
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
