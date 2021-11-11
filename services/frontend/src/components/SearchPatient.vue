<template>
  <div class="search-bar flex-column-items-start">
    <label> Wyszukaj pacjenta po peselu lub numerze paszportu </label> 
    <div class="flex-row-items-start">
      <select 
        id="patient-id-type-selector"
        class="input-element-standard input-element-addon keyboard-input input-element-small"
        name="patient-id-type"
        @change="changePatientIdType($event)"
      >
        <option value="pesel">Pesel</option>
        <option value="passport-id">Nr paszportu</option>
      </select>
      <input
        id="patient-id"
        class="input-element-standard input-element-addon keyboard-input"
        v-bind:type="[patientIdType=='pesel' ? 'number': 'text']"
        v-bind:name="patientIdType"
        v-bind:placeholder="[patientIdType=='pesel' ? 'Pesel...': 'Nr paszportu...']"
        autocomplete="off"
      />
    </div>
    <label style="margin-block-start: 30px"> Wyszukaj pacjenta po imieniu i nazwisku </label> 
    <div class="flex-row-items-start">
      <input
        class="input-element-standard input-element-addon keyboard-input"
        type="text"
        name="first-name"
        placeholder="Pierwsze Imię..."
        autocomplete="off"
      />
      <input
        class="input-element-standard input-element-addon keyboard-input"
        type="text"
        name="second-name"
        placeholder="Drugie Imię (opcjonalnie)..."
        autocomplete="off"
      />
      <input
        class="input-element-standard input-element-addon keyboard-input"
        type="text"
        name="surname"
        placeholder="Nazwisko..."
        autocomplete="off"
      />
       
    </div>
    <input
      class="input-element-standard input-element-addon keyboard-input"
      type="button"
      name="submit"
      value="Wyszukaj"
      v-on:click="searchPatient(1)"
    />
  </div>  
</template>

<script>

export default {
  name: 'SearchPatient',
  props: ['searchPatient'],
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
.search-bar {
  background-color: var(--color-sector);
  border-bottom-left-radius: 3px;
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
  padding: 25px;
  font-size: 1rem;
  overflow: hidden;
}

.input-element-addon {
  margin-inline-start: 20px;
}
</style>
