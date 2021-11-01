<template>
  <form class="signUpBox">
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
  width: -webkit-fit-content;
  height: -webkit-fit-content;
  width: -moz-fit-content;
  height: -moz-fit-content;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  font-size: 2rem;
  font-family: "Balsamiq Sans", cursive;
  color: var(--color-text);
}


.input-element-standard, .input-file-field::-webkit-file-upload-button {
  background-color: var(--color-accent);
  margin-block-start: 20px;
  border: none;
  border-radius: 3px;
  padding-block: 10px;
  padding-inline: 15px;
  font-family: "Balsamiq Sans", cursive;
  color: var(--color-text);
}

.input-element-standard:hover, .input-file-field::-webkit-file-upload-button:hover {
    filter: brightness(95%);
}

.input-element-small {
    padding: 8px !important;
    font-size: 0.8rem;
}

.keyboard-input:focus {
  outline: none;
}

.keyboard-input::placeholder {
  color: var(--color-text-darker);
  opacity: 1; 
}

.keyboard-input:-ms-input-placeholder {
  color: var(--color-text-darker);
}

.button {
  margin-block-start: 10px !important;
  font-size: 1rem;  
}

.link {
  background-color: transparent !important;
  text-decoration: none;
  font-size: 0.8rem !important;
}

.link:hover {
  filter: brightness(95%);
}
</style>