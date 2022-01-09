<template>
  <div class="warning-page">
    Brak dostępu
    <router-link to="/" class="go-home"> Powróć do strony głównej </router-link>
  </div>
</template>

<script>
export default {
  name: 'PageNotFound',
  components: {
  },
}
</script>

<style>
.warning-page {
  background-color: orangered;
  font-size: 2vw;
  color: white;
  width: 100vw;
  height: 100vh;
}

.go-home {
    text-decoration: none;
    color: white
}
</style>
