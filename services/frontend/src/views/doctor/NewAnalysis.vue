<template>
  <div>
    <SearchUser v-if="showSearchBox" v-bind:searchUser="searchUser" v-bind:userType="'patient'" />
    <div v-else>
      <h1 > Wybrany pacjent - {{ `${this.patientInfo["first_name"]} ${this.patientInfo["second_name"]} ${this.patientInfo["last_name"]}`}}</h1>
      <AnalysisInit v-bind:patientID="chosenUserId"  />
    </div>
  </div>
</template>

<script>
import AnalysisInit from '../../components/AnalysisInit.vue'
import SearchUser from '../../components/SearchUser.vue'

export default {
  name: 'NewAnalysis',
  components: {
    AnalysisInit,
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
