<template>
  <div class="patient-data-table">
    <v-card class="card" elevation="2">
            <v-card-title>Dane pacjenta </v-card-title>
            <v-card-text>
              <div>Pesel: {{ patientData.pesel }}</div>
              <div>Imie: {{ patientData.first_name }}</div>
              <div v-if="patientData.second_name != null">Drugie imie: {{ patientData.second_name }}</div>
              <div>Nazwisko: {{ patientData.last_name }} </div>
            </v-card-text> 
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'PatientTable',
  props: ['patientData'],
}
</script>

<style scoped>

</style>
