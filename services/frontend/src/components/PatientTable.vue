<template>
  <div class="patient-data-table">
    <v-card :loading=load class="card" elevation="2">
            <v-card-title>Dane pacjenta </v-card-title>
            <v-card-text>
              <div>PESEL: {{ patientData.pesel }}</div>
              <div>Imię: {{ patientData.first_name }}</div>
              <div v-if="patientData.second_name != null">Drugie imię: {{ patientData.second_name }}</div>
              <div>Nazwisko: {{ patientData.last_name }} </div>
            </v-card-text> 
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'PatientTable',
  props: ['patientData', "loading"],
  computed: {
    load() {
      return this.loading
    }
  }
}
</script>

<style scoped>

</style>
