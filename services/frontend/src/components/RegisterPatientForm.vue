<template>
  <form class="register-patient-box sector flex-column-items-centered">
    Zarejestruj pacjenta
    <input
      class="input-element-standard keyboard-input"
      type="text"
      name="email"
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
      value="Zarejestruj pacjenta"
    />
  </form>
</template>

<script>

export default {
  name: "RegisterPatientForm",
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
