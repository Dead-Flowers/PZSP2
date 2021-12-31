<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <SetupPasswd v-bind:usertype="'doctor'" />
  </div>
</template>

<script>
import SetupPasswd from '../../components/SetupPasswd.vue'


export default {
  name: 'FirstLogin',
  components: {
    SetupPasswd
  },
  
}
</script>

<style>
</style>
