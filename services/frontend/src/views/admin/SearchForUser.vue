<template>
  <div>
    <h1>{{ header }}</h1>
    <v-divider/>
    <SearchUser v-bind:searchUser="searchUser" v-bind:userTypes="['patient', 'doctor', 'admin']" />
  </div>
</template>

<script>
import SearchUser from '../../components/SearchUser.vue'
import router from '../../router';

export default {
  name: 'SearchForUser',
  components: {
    SearchUser,
  },
  data() {
    return {
    }
  },
  computed: {
    header() {
      return this.targetPage == 'reset-password' ? 'Reset Hasła Użytkownika'
             : null;
    },
    targetPage() {
      return this.$route.params.target;
    }
  },
  methods: {
    searchUser(user) {
        router.push(`/admin/${this.targetPage}/${user.id}`) 
    },
    
  },
  beforeMount() {
    
  },
}
</script>

<style>

</style>
