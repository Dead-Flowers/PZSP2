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
      if (this.passwordAuth()) {
        if (this.newPassword != this.newPasswordConfirm) 
        {
          this.rejectPasswordChangeByNotMatch();
          return;
        } 
        this.acceptPasswordChange();
      }
      else this.rejectPasswordChangeByAuth();
    },
    passwordAuth() {
      // this is a mock
      return this.currentPassword == "test";
    },
    acceptPasswordChange() {
      // do sth
      alert("Zmiana hasła udana");
    },
    rejectPasswordChangeByAuth() {
      this.oldPassword=null;
      this.newPassword=null;
      this.newPasswordConfirm=null;
      alert("Niepoprawne obecne hasło");
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