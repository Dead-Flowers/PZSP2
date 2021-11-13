<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <AnalysisInit />
    <Navbar />
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue'
import AnalysisInit from '../components/AnalysisInit.vue'

export default {
  name: 'NewAnalysis',
  components: {
    AnalysisInit,
    Navbar
  },
}
</script>

<style>
</style>
