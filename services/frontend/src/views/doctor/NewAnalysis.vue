<template>
  <div class="max-screen-space-container flex-row-items-start">
    <Navbar v-bind:usertype="'doctor'" />
    <div class="navbar-as-adjacent flex-column-items-centered">
        <div class="sector">
          <SearchUser v-if="showSearchBox" v-bind:searchUser="searchUser" v-bind:userType="'patient'" />
          <div v-else>
            <h1 > Wybrany pacjent - {{ `${this.patientInfo["first_name"]} ${this.patientInfo["second_name"]} ${this.patientInfo["last_name"]}`}}</h1>
            <AnalysisInit v-bind:patientID="chosenUserId"  />
          </div>
        </div>
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
      patientInfo: {},
      chosenUserId: null,
    }
  },
  methods: {
    searchUser(user) {
      this.showSearchBox = false;
      this.patientInfo = user;
      this.chosenUserId = user.id
      console.log(user.id)
    },
  }
}
</script>

<style>
</style>
