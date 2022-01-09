<template>
  <v-form
    ref="form"
    v-model="valid"
    @submit="(e) => {e.preventDefault(); checkPasswordChange();}"
  >
    <h1> Zmiana Hasła</h1>
    
    <v-text-field
      v-model="currentPassword"
      :rules="rules.required"
      type="password"
      label="Obecne hasło"
    />

    <v-text-field
      v-model="newPassword"
      :rules="rules.newPassword"
      type="password"
      label="Nowe hasło"
    />

    <v-text-field
      v-model="newPasswordConfirm"
      :rules="rules.newPasswordConfirm"
      type="password"
      label="Powtórz nowe hasło"
    />

    <v-btn
      v-bind:disabled="!valid"
      color="success"
      class="mr-4"
      type="submit"
    >
      Zmień hasło
    </v-btn>
  </v-form>
</template>

<script>

export default {
  name: 'ChangePassword',
  data() {
    return {
      currentPassword: null,
      newPassword: null,
      newPasswordConfirm: null,
      rules: { 
        required: [
          v => !!v || 'Wymagane pole',
        ],
        newPassword: [
          v => !!v || 'Wymagane pole',
          v => /^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z]).{8,}$/.test(v) || 'Hasło musi zawierać dużą i małą literę, liczbę i znak specjalny',
        ],
        newPasswordConfirm: [
          v => !!v || 'Wymagane pole',
          v => v == this.newPassword || 'Hasła muszą być identyczne'
        ],
      },
      valid: false,
    }
  },
  methods: {
    checkPasswordChange() {
      //todo check if currentPassword is correct
      
      this.passwordChange();
    },
    async passwordChange() {
      let payload = {
        password: this.newPassword
      }
      
      await this.$store.dispatch("actionUpdateMe", payload)

      alert("Zmiana hasła udana");
    },
  }
}
</script>

<style scoped>
.change-password-box {
  padding-block: 2vw;
  padding-inline: 2.5vw;
  font-size: 2vw;
}
</style>