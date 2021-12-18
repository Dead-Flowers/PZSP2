<template>
  <form class="register-patient-box sector flex-column-items-centered">
    Zarejestruj doktora
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="email"
      placeholder="Email..."
      autocomplete="off"
    />
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="first-name"
      placeholder="Pierwsze Imię..."
      autocomplete="off"
    />
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="second-name"
      placeholder="Drugie Imię (opcjonalnie)..."
      autocomplete="off"
    />
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="surname"
      placeholder="Nazwisko..."
      autocomplete="off"
    />
    <input
      class="input-element-standard button"
      type="button"
      value="Zarejestruj doktora"
    />
  </form>
</template>

<script>

export default {
  name: "RegisterDoctorForm",
  data() {
    return {
      patientIdType: 'pesel',
    }
  },
  methods: {
    changePatientIdType(event) {
      this.patientIdType = event.target.value;
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
