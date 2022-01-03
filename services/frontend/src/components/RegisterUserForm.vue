<template>
  <v-form
    ref="form"
    v-model="valid" 
    @submit="(e) => {e.preventDefault(); submitRegistration();}"
  >
    <h1 v-if="registationDone"> Rejestracja zakończona  </h1> 
    <small v-if="registationDone">  Zapisz hasło dla użytkownika: {{ password }} </small>
    <h1 v-if="registationError"> Problem z rejestracją </h1>
    <h1 v-else> Zarejestruj {{this.wording}} </h1> 
     <v-select
      v-model="userIdType"
      :items="userIdTypeList"
      label="Rodzaj numeru identyfikacyjnego"
    />
    <v-text-field
      id="user-id"
      v-model="userId"
      v-bind:label="userIdType=='pesel' ? 'Pesel...': 'Nr paszportu...'"
      v-bind:rules="userIdType=='pesel' ? rules.pesel : rules.required"
    />
    <v-text-field
      v-model="email"
      :rules="rules.email"
      label="E-mail"
    />
    <v-text-field
      v-model="firstName"
      :rules="rules.required"
      label="Pierwsze Imię"
    />
    <v-text-field
      v-model="secondName"
      label="Drugie Imię"
    />
    <v-text-field
      v-model="last_name"
      :rules="rules.required"
      label="Nazwisko"
    />
    <v-select
      v-model="sex"
      :items="sexList"
      label="Wybierz płeć"
    />
    <v-menu
        ref="menu"
        v-model="menu"
        :close-on-content-click="false"
        :return-value.sync="birthDate"
        transition="scale-transition"
        offset-y
        min-width="auto"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="birthDate"
            label="Data urodzenia"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="birthDate"
          no-title
          scrollable
        >
          <v-spacer></v-spacer>
          <v-btn
            text
            color="primary"
            @click="menu = false"
          >
            Cancel
          </v-btn>
          <v-btn
            text
            color="primary"
            @click="$refs.menu.save(birthDate)"
          >
            OK
          </v-btn>
        </v-date-picker>
      </v-menu>
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
  name: "RegisterUserForm",
  props: ['usertype'],
  data() {
    return {
      menu: false,
      birthDate: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
      registationDone: false,
      registationError: false,
      userIdType: 'pesel',
      userIdTypeList: ['pesel', 'id paszportu'],
      sex: null,
      sexList: ['Meżczyzna', 'Kobieta', 'Inna'],
      firstName: null,
      secondName: null,
      last_name: null,
      email: null,
      userId: null,
      password: null,
      wording: null,
      rules: {
        email: [
          v => !!v || 'Wymagane pole',
          v => /.+@.+\..+/.test(v) || 'E-mail musi być poprawny',
        ],
        pesel: [
          v => !!v || 'Wymagane pole',
          v => /^[0-9]{11}$/.test(v) || 'Pesel musi zawierać 11 cyfr',
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
    if (this.usertype == 'patient') this.wording = 'pacjenta';
    if (this.usertype == 'doctor') this.wording = 'doktora';
  },
  methods: {
    async submitRegistration(){
      this.password = generatePassword()
      let payload = {
        userIdType: this.userIdType,
        first_name: this.firstName,
        second_name: this.secondName,
        last_name: this.last_name,
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
  padding-block: 2vw;
  padding-inline: 2.5vw;
  font-size: 2vw;
}

</style>
