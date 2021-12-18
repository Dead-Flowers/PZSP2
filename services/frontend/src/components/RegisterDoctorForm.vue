<template>
  <form class="register-patient-box sector flex-column-items-centered">
    Zarejestruj doktora
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="email"
      placeholder="Email..."
      autocomplete="off"
      v-model="email"
    />
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="first-name"
      placeholder="Pierwsze Imię..."
      autocomplete="off"
      v-model="firstName"
    />
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="second-name"
      placeholder="Drugie Imię (opcjonalnie)..."
      autocomplete="off"
      v-model="secondName"
    />
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="surname"
      placeholder="Nazwisko..."
      autocomplete="off"
      v-model="surname"
    />
    <input
      class="input-element-standard button"
      type="button"
      value="Zarejestruj doktora"
      @click="registerDoc"
    />
  </form>
</template>

<script>

export default {
  name: "RegisterDoctorForm",
  data() {
    return {
      firstName: null,
      secondName: null,
      surname: null,
      email: null,
    }
  },
  methods: {
    registerDoc() {
      let data_packet = this.parsedata();
      console.log(data_packet); //this is here only so vue does not cry
      // backend connection here
      this.resetForm();
    },
    parsedata() {
      return {
        "firstName": this.firstName,
        "secondName": this.secondName,
        "surname": this.surname,
        "email": this.email,
      }
    },
    resetForm() {
      this.firstName =  null;
      this.secondName = null;
      this.surname = null;
      this.email = null;
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
</style>
