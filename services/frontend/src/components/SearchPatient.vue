<template>
  <div class="search-area">
    <div class="search-icon"> Wyszukaj pacjenta </div>
    <div class="search-bar">
      <label> Wyszukaj pacjenta po peselu lub numerze paszportu </label> 
      <div class="searchOption">
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
      </div>
      <label style="margin-block-start: 30px"> Wyszukaj pacjenta po imieniu i nazwisku </label> 
      <div class="searchOption">
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
      </div>
    </div>  
  </div>
</template>

<script>

export default {
  name: 'SearchPatient',
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
.search-icon {
  background-color: var(--color-search);
  border: 0;
  border-radius: 3px;
  padding: 10px;
  font-size: 1rem;
  font-family:  "Roboto", sans-serif;
  color: var(--color-text);
}

.search-bar {
  position: absolute;
  z-index: 5;
  background-color: var(--color-search);
  border-bottom-left-radius: 3px;
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
  padding: 25px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  
  font-size: 1rem;
  font-family:  "Roboto", sans-serif;
  color: var(--color-text);
  overflow: hidden;
  visibility: hidden;
}

.search-area:hover .search-bar {
  visibility: visible !important;
}

.search-area:hover .search-icon {
  border-bottom-left-radius: 0px;
  border-bottom-right-radius: 0px;
}
.search-option {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: flex-start;
}

.input-element-standard {
  background-color: var(--color-accent);
  margin-inline-start: 20px;
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
