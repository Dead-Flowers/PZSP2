<template>
  <form class="signUpBox flex-column-items-centered">
    Zarejestruj się
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="email"
      placeholder="Email..."
      autocomplete="off"
    />
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="login"
      placeholder="Login..."
      autocomplete="off"
    />
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
    <div>
      <input
        class="input-element-standard button"
        style="margin-inline-end: 20px"
        type="submit"
        value="Zaloguj się"
      />
      <input
        class="input-element-standard button"
        type="button"
        value="Zarejestruj się"
      />
    </div>
  </form>
</template>

<script>
export default {
  name: 'Register'
}
</script>

<style scoped>
.signUpBox {
  padding-block: 40px;
  padding-inline: 50px;
  font-size: 2rem;
}
</style>