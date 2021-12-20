<template>
  <div class="max-screen-space-container flex-row-items-start">
    <Navbar v-bind:usertype="'doctor'" />
    <div class="navbar-as-adjacent flex-column-items-centered">
      <SearchUser v-if="showSearchBox" v-bind:searchUser="searchUser" v-bind:userType="'patient'" />
      <AnalysisInit v-bind:patientID="chosenUserId"  v-else />
    </div>
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
      patientData: {},
      chosenUserId: null,
    }
  },
  methods: {
    searchUser(user) {
      this.showSearchBox = false;
      this.chosenUserId = user.id
      console.log(user.id)
    },
  }
}
</script>

<style>
</style>
