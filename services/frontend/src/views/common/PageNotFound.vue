<template>
  <div @click="goToFrontPage" class="er404">
    <h1>Błąd 404 Nie znaleziono strony</h1>
    <hr />
    <h2>Powrót</h2>
  </div>
</template>

<script>
import router from '../../router'
export default {
  name: 'PageNotFound',
  components: {
  },
  methods: {
    goToFrontPage() {
      if (this.$store.getters["isLoggedIn"]) {
        router.push(`/${this.$store.getters["userType"]}/home`);
      }
      else {
        router.push("/");
      }
    }
  }
}
</script>

<style>
.er404 {
  color: red;
}

.er404:hover {
  color:maroon;
}
</style>
