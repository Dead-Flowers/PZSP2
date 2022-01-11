<template>
  <div @click="goToCorrectPage" class="er404">
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
    goToCorrectPage() {
      const userType = `${this.$store.getters["userType"]}`;
      if (this.$store.getters["isLoggedIn"] && userType && userType != 'null') {
        router.push(`/${userType}/home`);
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
