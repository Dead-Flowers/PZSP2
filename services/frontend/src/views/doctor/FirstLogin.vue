<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <SetupPasswd v-bind:usertype="'doctor'" />
  </div>
</template>

<script>
import SetupPasswd from '../../components/SetupPasswd.vue'
import '../../../public/style.css'

export default {
  name: 'FirstLogin',
  components: {
    SetupPasswd
  },
  
}
</script>

<style>
</style>
