<template>
  <form class="register-patient-box sector flex-column-items-centered">
    <div v-if="registationDone"> Rejestracja zakończona  </div> 
    <div v-else> Zarejestruj Doktora  </div> 
    <div v-if="registationDone" class="save-password-box">  Zapisz hasło dla Doktora: {{ password }} </div>
    <div v-if="registationError"> Problem z rejestracją </div>
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="email"
      placeholder="Email..."
      v-model="email"
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
      v-model="surname"
      placeholder="Nazwisko..."
      autocomplete="off"
    />
    <input
      class="input-element-standard button"
      type="button"
      value="Zarejestruj doktora"
      @click="submitRegistration"
    />
  </form>
</template>

<script>
import { generatePassword } from "@/utils.js"

export default {  
  name: "RegisterDoctorForm",
  data() {
    return {
      registationDone: false,
      registationError: false,
      fistName: null,
      secondName: null,
      surname: null,
      email: null,
      password: null,
    }
  },
  beforeMount() {
    this.$store.commit("resetRegistration")
  },
  methods: {
    async submitRegistration(){
      this.password = generatePassword()
      let payload = {
        first_name: this.fistName,
        second_name: this.secondName,
        last_name: this.surname,
        email: this.email,
        password: this.password,
        role: "doctor"
      }
      await this.$store.dispatch("actionRegister",  payload)
      
      this.registationDone = this.$store.getters["registrationSuccess"]
      this.registationError = this.$store.getters["registrationError"]
    }
  }
}
</script>

<style scoped>
.register-patient-box {
  padding-block: 40px;
  padding-inline: 50px;
  font-size: 2rem;
}

.save-password-box{
  font-size: 1rem
}
</style>
