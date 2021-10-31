<template>
  <div class="sign-in-container">
    <form class="sign-in-box">
      Witaj, zaloguj się!
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
  </div>
</template>

<script>
export default {
  name: 'Login'
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