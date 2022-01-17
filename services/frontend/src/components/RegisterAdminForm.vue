<template>
  <v-form
    ref="form"
    v-model="valid" 
    @submit="(e) => {e.preventDefault(); submitRegistration();}"
  > 
    <div v-if="registationDone">
      <h1> Rejestracja zakończona  </h1> 
      <h3>  Zapisz hasło dla administratora: {{ password }} </h3>
      <v-divider/>
    </div>
    <h1 v-if="registationError"> Problem z rejestracją </h1>
    <h2 v-else> Zarejestruj Administratora </h2> 
    
    <v-text-field
      v-model="email"
      :rules="rules.email"
      label="E-mail"
    />
    <v-text-field
      v-model="first_name"
      :rules="rules.required"
      label="Pierwsze Imię"
    />
    <v-text-field
      v-model="second_name"
      label="Drugie Imię"
    />
    <v-text-field
      v-model="last_name"
      :rules="rules.required"
      label="Nazwisko"
    />
    <v-btn
      v-bind:disabled="!valid"
      color="success"
      class="mr-4"
      type="submit"
    >
      Zarejestruj
    </v-btn>
  </v-form>
</template>

<script>
import { generatePassword } from "@/utils.js"

export default {
  name: "RegisterAdminForm",
  data() {
    return {
      menu: false,
      registationDone: false,
      registationError: false,
      email: null,
      first_name: null,
      second_name: null,
      last_name: null,
      userId: null,
      password: null,
      rules: {
        email: [
          v => !!v || 'Wymagane pole',
          v => /.+@.+\..+/.test(v) || 'E-mail musi być poprawny',
        ],
        required: [
          v => !!v || 'Wymagane pole',
        ],
        valid: false,
      }
    }

  },
  beforeMount() {
    this.$store.commit("resetRegistration");
  },
  methods: {
    async submitRegistration(){
      this.password = generatePassword()
      let payload = {
        first_name: this.first_name,
        second_name: this.second_name,
        last_name: this.last_name,
        email: this.email,
        password: this.password,
        role: 'admin',
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
  padding-block: 2vw;
  padding-inline: 2.5vw;
  font-size: 2vw;
}

</style>
