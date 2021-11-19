<template>
  <div class="sector flex-column-items-start">
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
        v-model="patientId"
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
        v-model="firstName"
        autocomplete="off"
      />
      <input
        class="input-element-standard input-element-addon keyboard-input"
        type="text"
        name="second-name"
        placeholder="Drugie Imię (opcjonalnie)..."
        v-model="secondName"
        autocomplete="off"
      />
      <input
        class="input-element-standard input-element-addon keyboard-input"
        type="text"
        name="surname"
        placeholder="Nazwisko..."
        v-model="surname"
        autocomplete="off"
      />   
    </div>
    <input
      class="input-element-standard input-element-addon"
      type="button"
      name="button"
      value="Wyszukaj"
      @click="searchForPatient"
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
      patientId: null,
      firstName: null,
      secondName: null,
      surname: null,
    }
  },
  methods: {
    changePatientIdType(event) {
      this.patientIdType = event.target.value;
    },
    searchForPatient() {
      if (this.verifyPatient()) {
        this.patientFound();
      }
      else {
        this.patientNotFound();
      }
    },
    verifyPatient () {
      return this.patientId=='11111' || `${this.firstName} ${this.secondName} ${this.surname}`=="Bonifacy Rupert Gąska";
    },
    patientFound() {
      this.searchPatient();
    },
    patientNotFound() {
      alert('Nie znaleziono pacjenta');
    },
  }
}
</script>

<style scoped>
.input-element-addon {
  margin-inline-start: 20px;
}
</style>
