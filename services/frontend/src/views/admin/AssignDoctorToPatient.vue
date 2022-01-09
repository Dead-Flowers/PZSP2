<template>
  <div class="max-screen-space-container flex-row-items-start">
    <div class="navbar-as-adjacent flex-column-items-centered">
      <div  
        class="sector flex-column-items-centered"
        v-if="this.stage == 'noDoctor'"
      >
        <h1> Wyszukaj Doktora </h1>
        <SearchUser v-bind:searchUser="searchDoctor" v-bind:userType="'doctor'" />
      </div>
      <div 
        class="sector flex-column-items-centered"
        v-if="this.stage == 'hasDoctor'"
      >
        <h2> Wybrany doktor - {{ `${this.doctorInfo["first_name"]} ${this.doctorInfo["second_name"]} ${this.doctorInfo["last_name"]}`}}</h2>
        <h1> Wyszukaj Pacjenta </h1>
        <SearchUser v-bind:searchUser="searchPatient" v-bind:userType="'patient'" />
      </div>
      <div 
        class="sector flex-column-items-centered"
        v-if="this.stage == 'assigned'"
      >
        <h1> Sukces! Przyisano pacjenta do doktora. </h1>
        <h2> Wybrany doktor - {{ `${this.doctorInfo["first_name"]} ${this.doctorInfo["second_name"]} ${this.doctorInfo["last_name"]}`}}</h2>
        <h2> Wybrany pacjent - {{ `${this.patientInfo["first_name"]} ${this.patientInfo["second_name"]} ${this.patientInfo["last_name"]}`}}</h2>
        <v-btn
          color="success"
          class="mr-4"
          @click="newPatientSameDoctor"
        >
          Przypisz nowego pacjenta do tego samego doktora
        </v-btn>
        <v-btn
          color="success"
          class="mr-4"
          @click="newPatientNewDoctor"
        >
          Przypisz nowego pacjenta do innego doktora
        </v-btn>
      </div>
    </div>
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
