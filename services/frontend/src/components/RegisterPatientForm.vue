<template>
  <form class="register-patient-box sector flex-column-items-centered">
    <div v-if="registationDone"> Rejestracja zakończona  </div> 
    <div v-else> Zarejestruj pacjenta  </div> 
    <div v-if="registationDone" class="save-password-box">  Zapisz hasło dla pacjeta: {{ password }} </div>
    <div v-if="registationError"> Problem z rejestracją </div>
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="email"
      v-model="email"
      placeholder="Email..."
      autocomplete="off"
    />
    <select 
      id="patient-id-type-selector"
      class="input-element-standard keyboard-input input-element-small"
      name="patient-id-type"
      @change="changePatientIdType($event)"
    >
      <option value="pesel">Pesel</option>
      <option value="passport-id">Nr paszportu</option>
    </select>
    <input
      id="patient-id"
      class="input-element-standard keyboard-input"
      v-bind:type="[patientIdType=='pesel' ? 'number': 'text']"
      v-bind:name="patientIdType"
      v-bind:placeholder="[patientIdType=='pesel' ? 'Pesel...': 'Nr paszportu...']"
      v-model="patientId"
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
      v-model="surName"
      autocomplete="off"
    />
    <input
      class="input-element-standard button"
      type="button"
      value="Zarejestruj pacjenta"
      @click="submitRegistration"
    />
  </form>
</template>

<script>
import { generatePassword } from "@/utils.js"

export default {
  name: "RegisterPatientForm",
  data() {
    return {
      registationDone: false,
      registationError: false,
      patientIdType: 'pesel',
      fistName: null,
      secondName: null,
      surName: null,
      email: null,
      patientId: null,
      password: null,
    }
  },
  beforeMount() {
    this.$store.commit("resetRegistration")
  },
  methods: {
    changePatientIdType(event) {
      this.patientIdType = event.target.value;
    },
    async submitRegistration(){
      this.password = generatePassword()
      let payload = {
        patientIdType: this.patientIdType,
        first_name: this.fistName,
        second_name: this.secondName,
        last_name: this.surName,
        email: this.email,
        patient_id: this.patientId,
        password: this.password,
        role: "patient"
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
