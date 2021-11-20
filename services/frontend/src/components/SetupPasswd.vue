<template>
  <form class="sector flex-column-items-centered">
    <label >Witaj {{userName}}.</label>
    <label>Logujesz się po raz pierwszy. Ustaw hasło.</label>
    <input
    class="input-element-standard keyboard-input"
    type="password"
    name="password"
    placeholder="Hasło..."
    autocomplete="off"
    />
    <input
      class="input-element-standard keyboard-input"
      type="password"
      name="password-confirm"
      placeholder="Powtórz Hasło..."
      autocomplete="off"
    />
    <input
      class="input-element-standard button"
      type="button"
      value="Ustaw"
      @click="setPasswd('test')"
    />
  </form>
</template>

<script>
export default {
  name: 'SetupPasswd',
  props: ['userName'],
  methods: {
    setPasswd: function (msg) {
      console.log('Setup password', msg)
    }
  },
}
</script>

<style scoped>

</style>