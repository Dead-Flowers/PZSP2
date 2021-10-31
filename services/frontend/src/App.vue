<template>
  <div id="app">
    <Navbar />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'

export default {
  name: 'App',
  components: {
  Navbar
  }
}
</script>

<style>
.app {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
</style>
