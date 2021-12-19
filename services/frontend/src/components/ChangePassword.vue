<template>
  <form class="change-password-box sector flex-column-items-centered">
    Zmień hasło
    <input
      class="input-element-standard keyboard-input"
      type="password"
      name="currentPassword"
      placeholder="Obecne hasło..."
      v-model="currentPassword"
      autocomplete="off"
    /> 
    <input
      class="input-element-standard keyboard-input"
      type="password"
      name="newPassword"
      placeholder="Nowe hasło..."
      v-model="newPassword"
      autocomplete="off"
    />
    <input
      class="input-element-standard keyboard-input"
      type="password"
      name="newPasswordConf"
      placeholder="Powtórz nowe hasło..."
      v-model="newPasswordConfirm"
      autocomplete="off"
    />
    <input
      class="input-element-standard button"
      type="button"
      value="Zmień hasło"
      @click="checkPasswordChange"
    />
  </form>
</template>

<script>

export default {
  name: 'ChangePassword',
  data() {
    return {
      currentPassword: null,
      newPassword: null,
      newPasswordConfirm: null,
    }
  },
  methods: {
    checkPasswordChange() {
      if (this.newPassword != this.newPasswordConfirm) 
      {
        this.rejectPasswordChangeByNotMatch();
        return;
      } 
      this.passwordChange();
    },
    async passwordChange() {
      let payload = {
        password: this.newPassword
      }
      
      await this.$store.dispatch("actionUpdateMe", payload)

      alert("Zmiana hasła udana");
    },
    rejectPasswordChangeByNotMatch() {
      this.oldPassword=null;
      this.newPassword=null;
      this.newPasswordConfirm=null;
      alert("Nowe hasło nie zostało poprawnie powtórzone!");
    },
  }
}
</script>

<style scoped>
.change-password-box {
  padding-block: 40px;
  padding-inline: 50px;
  font-size: 2rem;
}
</style>