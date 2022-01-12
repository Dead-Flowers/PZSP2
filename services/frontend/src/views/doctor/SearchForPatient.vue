<template>
  <div>
    <h1>{{ header }}</h1>
    <v-divider/>
    <SearchUser v-bind:searchUser="searchUser" v-bind:userType="'patient'" />
  </div>
</template>

<script>
import SearchUser from '../../components/SearchUser.vue'
import router from '../../router';

export default {
  name: 'SearchForPatient',
  components: {
    SearchUser,
  },
  data() {
    return {
    }
  },
  computed: {
    header() {
      return this.targetPage == 'new-analysis' ? 'Nowa analiza'
             : this.targetPage == 'recordings' ? 'Nagrania'
             : this.targetPage == 'patient-data' ? 'Dane pacjenta'
             : null
    },
    targetPage() {
      return this.$route.params.target;
    }
  },
  methods: {
    searchUser(user) {
        router.push(`/doctor/${this.targetPage}/${user.id}`) 
    },
    
  },
  beforeMount() {
    
  },
}
</script>

<style>

</style>
