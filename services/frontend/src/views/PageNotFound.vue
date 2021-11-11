<template>
  <div id="page-not-found" class="max-screen-space-container flex-column-items-centered">
    Nie znaleziono strony
    <router-link to="/" id="go-home" > Powróć do strony głównej </router-link>
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
#page-not-found {
  background-color: red;
  font-size: 2rem;
  color: white;
}

#go-home {
  text-decoration: none;
  font-size: 2rem;
  color: white;
}

#go-home:hover {
  filter: brightness(80%);
}
</style>
