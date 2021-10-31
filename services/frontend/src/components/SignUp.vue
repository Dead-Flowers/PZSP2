<template>
  <div class="sign-up-container">
    <form class="sign-up-box">
      Zarejestruj się poniżej!
      <input
        class="inputElementStandard keyboardInput"
        type="text"
        name="email"
        placeholder="Email..."
        autocomplete="off"
      />
      <input
        class="inputElementStandard keyboardInput"
        type="text"
        name="login"
        placeholder="Login..."
        autocomplete="off"
      />
      <input
        class="inputElementStandard keyboardInput"
        type="password"
        name="password"
        placeholder="Hasło..."
        autocomplete="off"
      />
      <input
        class="inputElementStandard keyboardInput"
        type="password"
        name="passwordConfirm"
        placeholder="Powtórz Hasło..."
        autocomplete="off"
      />
      <div>
        <input
          class="inputElementStandard button"
          type="submit"
          value="Masz konto? Zaloguj się"
        />
        <input
          class="inputElementStandard button"
          type="button"
          value="Zarejestruj"
        />
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Register'
}
</script>

<style>
.sign-in-box {
  background-color: var(--color-sector);
  border-radius: 3px;
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


.input-element-standard {
  background-color: var(--color-accent);
  margin-block-start: 20px;
  border: none;
  border-radius: 3px;
  padding-block: 10px;
  padding-inline: 15px;
  font-family: "Balsamiq Sans", cursive;
  color: var(--color-text);
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

.button:hover {
  filter: brightness(85%);
}

.link {
  background-color: transparent !important;
  text-decoration: none;
  font-size: 0.8rem !important;
}

.link:hover {
  filter: brightness(85%);
}

</style>