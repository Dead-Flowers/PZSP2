<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <SetupPasswd v-bind:userName="userName" />
  </div>
</template>

<script>
import SetupPasswd from '../components/SetupPasswd.vue'

export default {
  name: 'FirstLogin',
  components: {
    SetupPasswd
  },
  data() {
    return {
      userName: "Testowy użytkownik"
    }
  }
}
</script>

<style>
</style>
