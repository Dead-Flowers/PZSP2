<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <Navbar v-bind:usertype="'doctor'" />
    <SearchUser v-if="showSearchBox" v-bind:searchUser="searchUser" v-bind:userType="'patient'" />
    <AnalysisInit v-else />
  </div>
</template>

<script>
import Navbar from '../../components/Navbar.vue'
import AnalysisInit from '../../components/AnalysisInit.vue'
import SearchUser from '../../components/SearchUser.vue'

export default {
  name: 'NewAnalysis',
  components: {
    AnalysisInit,
    Navbar,
    SearchUser,
  },
  data() {
    return {
      showSearchBox: true,
      patientData: {}
    }
  }
}
</script>

<style>
</style>
