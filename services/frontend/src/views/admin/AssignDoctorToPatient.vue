<template>
  <div>
      <h1>Przypisywanie pacjenta</h1>
      <v-divider/>
      <!-- Wybor doktora -->
      <div
        v-if="this.stage == 'noDoctor'"
      >
        <h2> Wyszukaj Doktora </h2>
        <SearchUser v-bind:searchUser="searchDoctor" v-bind:userTypes="['doctor']" />
      </div>

      <!-- Wybrano doktora, wybor pacjenta -->
      <div
        style="display:flex"
        v-if="this.stage == 'hasDoctor'"
      >     
        <div>
          <h2> Wyszukaj Pacjenta </h2>
          <SearchUser v-bind:searchUser="searchPatient" v-bind:userTypes="['patient']" />
        </div>
        <v-card>
          <v-card-title>Dane Doktora </v-card-title>
          <v-card-text>
            <div>Pesel: {{ this.doctorInfo["pesel"] }}</div>
            <div>Imie: {{ this.doctorInfo["first_name"] }}</div>
            <div v-if="this.doctorInfo['second_name'] != null">Drugie imie: {{ this.doctorInfo['second_name'] }}</div>
            <div>Nazwisko: {{ this.doctorInfo['last_name'] }} </div>
          </v-card-text> 
        </v-card>
      </div>
      <!-- Przypisano pacjenta do doktora -->
      <v-container 
        class="sector flex-column-items-centered"
        v-if="this.stage == 'assigned'"
      >
        <v-row>
          <h2> Sukces! Przypisano pacjenta do doktora. </h2>
        </v-row>
        <v-row>
          <v-col>
            <v-card class="card">
              <v-card-title>Dane Doktora </v-card-title>
              <v-card-text>
                <div>Pesel: {{ this.doctorInfo["pesel"] }}</div>
                <div>Imie: {{ this.doctorInfo["first_name"] }}</div>
                <div v-if="this.doctorInfo['second_name'] != null">Drugie imie: {{ this.doctorInfo['second_name'] }}</div>
                <div>Nazwisko: {{ this.doctorInfo['last_name'] }} </div>
              </v-card-text> 
            </v-card>
          </v-col>
          <v-col>
            <v-card class="card">
              <v-card-title>Dane Pacjenta </v-card-title>
              <v-card-text>
                <div>Pesel: {{ this.patientInfo["pesel"] }}</div>
                <div>Imie: {{ this.patientInfo["first_name"] }}</div>
                <div v-if="this.patientInfo['second_name'] != null">Drugie imie: {{ this.patientInfo['second_name'] }}</div>
                <div>Nazwisko: {{ this.patientInfo['last_name'] }} </div>
              </v-card-text> 
            </v-card>
          </v-col>
        </v-row>
        <v-row>
            <v-btn
              color="success"
              class="mr-4 mb-2"
              @click="newPatientSameDoctor"
            >
              Przypisz nowego pacjenta do tego samego doktora
            </v-btn>
        </v-row>
        <v-row>
            <v-btn
              color="primary"
              class="mr-4"
              @click="newPatientNewDoctor"
            >
              Przypisz nowego pacjenta do innego doktora
            </v-btn>
        </v-row>
      </v-container>
  </div>
</template>

<script>
import SearchUser from '../../components/SearchUser.vue'
import { api } from '@/api';

export default {
  name: 'AssignDoctorToPatient',
  components: {
    SearchUser,
  },
  data() {
    return {
      patientId: null,
      patientInfo: null,
      doctorId: null,
      doctorInfo: null,
      stage: "noDoctor",
    }
  },
  methods: {
    searchPatient(patient) {
      if (patient.doctor_id) {
        const choice = window.confirm("Wybrany pacjent ma już przypisanego doktora. Czy na pewno chcesz kontynuować?");
        if (!choice) return;
      }
      this.patientInfo = patient;
      this.patientId = patient.id;
      this.assignD2P();
      this.stage = "assigned";
    },
    searchDoctor(user) {
      this.doctorInfo = user;
      this.doctorId = user.id;
      this.stage = "hasDoctor";
    },
    async assignD2P() {
      let newData = {
        doctor_id: this.doctorId,
      }
      const response = await api.updateUser(this.$store.getters["token"], this.patientId, newData);
      console.log(response);
    },
    newPatientSameDoctor() {
      this.stage = "hasDoctor";
      this.patientId = null;
      this.patientInfo = null;

    },
    newPatientNewDoctor() {
      this.stage = "noDoctor";
      this.patientId = null;
      this.patientInfo = null;
      this.doctorId = null;
      this.doctorInfo = null;
    },
  }
}
</script>

<style scoped>
label {
  font-size: 2vw;
  padding: 0.25vw;
  margin-block-start:  1.5vw;
}
.spacer {
  margin-inline-end: 2vw;
}
</style>
