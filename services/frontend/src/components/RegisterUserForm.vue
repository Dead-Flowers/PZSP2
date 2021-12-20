<template>
  <form class="register-user-box sector flex-column-items-centered">
    <div v-if="registationDone"> Rejestracja zakończona  </div> 
    <div v-else> Zarejestruj {{this.wording}} </div> 
    <div v-if="registationDone" class="save-password-box">  Zapisz hasło dla użytkownika: {{ password }} </div>
    <div v-if="registationError"> Problem z rejestracją </div>
    <select 
      id="user-id-type-selector"
      class="input-element-standard keyboard-input input-element-small"
      name="user-id-type"
      @change="changeUserIdType($event)"
    >
      <option value="pesel">Pesel</option>
      <option value="passport-id">Nr paszportu</option>
    </select>
    <input
      id="user-id"
      class="input-element-standard keyboard-input"
      type="text"
      v-bind:name="userIdType"
      v-bind:placeholder="[userIdType=='pesel' ? 'Pesel...': 'Nr paszportu...']"
      v-model="userId"
      autocomplete="off"
    />
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="email"
      v-model="email"
      placeholder="Email..."
      autocomplete="off"
    />
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="first-name"
      v-model="fistName"
      placeholder="Pierwsze Imię..."
      autocomplete="off"
    />
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="second-name"
      v-model="secondName"
      placeholder="Drugie Imię (opcjonalnie)..."
      autocomplete="off"
    />
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="surname"
      placeholder="Nazwisko..."
      v-model="surname"
      autocomplete="off"
    />
    <input
      class="input-element-standard button"
      type="button"
      value="Zarejestruj"
      @click="submitRegistration"
    />
  </form>
</template>

<script>
import { generatePassword } from "@/utils.js"

export default {
  name: "RegisterUserForm",
  props: ['usertype'],
  data() {
    return {
      registationDone: false,
      registationError: false,
      userIdType: 'pesel',
      fistName: null,
      secondName: null,
      surname: null,
      email: null,
      userId: null,
      password: null,
      wording: null,
    }
  },
  beforeMount() {
    this.$store.commit("resetRegistration");
    if (this.usertype == 'patient') this.wording = 'pacjenta';
    if (this.usertype == 'doctor') this.wording = 'doktora';
  },
  methods: {
    changeUserIdType(event) {
      this.userIdType = event.target.value;
    },
    async submitRegistration(){
      this.password = generatePassword()
      let payload = {
        userIdType: this.userIdType,
        first_name: this.fistName,
        second_name: this.secondName,
        last_name: this.surname,
        email: this.email,
        user_id: this.userId,
        password: this.password,
        role: this.usertype,
        pesel: this.userId,
      }
      await this.$store.dispatch("actionRegister",  payload)
      
      this.registationDone = this.$store.getters["registrationSuccess"]
      this.registationError = this.$store.getters["registrationError"]
    }
  }
}
</script>

<style scoped>
.register-user-box {
  padding-block: 40px;
  padding-inline: 50px;
  font-size: 2rem;
}
.save-password-box{
  font-size: 1rem
}
</style>
