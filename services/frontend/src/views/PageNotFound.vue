<template>
  <div id="page-not-found">
    Nie znaleziono strony
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
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  background-color: red;
  font-size: 4rem;
}
</style>
