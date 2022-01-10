<template>
  <div>
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
        targetPage: null,
    }
  },
  methods: {
    searchUser(user) {
        router.push(`/doctor/${this.targetPage}/${user.id}`) 
    },
    
  },
  beforeMount() {
    this.targetPage = this.$route.params.target
  },
}
</script>

<style>

</style>
