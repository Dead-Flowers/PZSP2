<template>
  <form class="register-patient-box">
    Zarejestruj pacjenta
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
  name: "RegisterPatient",
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
  width: -webkit-fit-content;
  height: -webkit-fit-content;
  width: -moz-fit-content;
  height: -moz-fit-content;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  
  font-size: 2rem;
  font-family:  "Roboto", sans-serif;
  color: var(--color-text);
}


.input-element-standard {
  background-color: var(--color-accent);
  margin-block-start: 20px;
  border: none;
  border-radius: 3px;
  padding-block: 10px;
  padding-inline: 15px;
  font-family:  "Roboto", sans-serif;
  color: var(--color-text);
}

.input-element-standard:hover {
    filter: brightness(95%);
}

.input-element-small {
    padding: 8px !important;
    font-size: 0.8rem;
}

.keyboard-input:focus {
  outline: none;
}

.keyboard-input::placeholder {
  color: var(--color-text-darker);
  opacity: 1; 
}

.keyboard-input:-ms-input-placeholder {
  color: var(--color-text-darker);
}

.keyboard-input::-webkit-inner-spin-button, 
.keyboard-input::-webkit-outer-spin-button { 
  -webkit-appearance: none; 
  margin: 0; 
}

.button {
  margin-block-start: 10px !important;
  font-size: 1rem;  
}

.link {
  background-color: transparent !important;
  text-decoration: none;
  font-size: 0.8rem !important;
}

.link:hover {
  filter: brightness(95%);
}
</style>
