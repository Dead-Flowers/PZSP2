<template>
  <form class="sign-in-box sector flex-column-items-centered">
    Witaj, zaloguj się
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
    />
    <a  
      class="input-element-standard button link"
      href="https://www.google.com"
    >
      Zapomniałeś hasła?
    </a>
    <div >
      <input
        class="input-element-standard button"
        type="submit"
        value="Zaloguj się"
        style="margin-inline-end: 20px"
      />
      <input
        class="input-element-standard button"
        type="button"
        value="Załóż konto"
      />
    </div>
  </form>
</template>

<script>
export default {
  name: 'Login'
}
</script>

<style scoped>
.sign-in-box {
  padding-block: 40px;
  padding-inline: 50px;
  font-size: 2rem;
}
</style>