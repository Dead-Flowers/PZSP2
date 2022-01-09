<template>
  <div class="max-screen-space-container flex-row-items-start">
    <div class="navbar-as-adjacent flex-column-items-centered">
      <div  
        class="sector flex-column-items-centered"
        v-if="this.stage == 'noDoctor'"
      >
        <label> Wyszukaj Doktora </label>
        <SearchUser v-bind:searchUser="searchDoctor" v-bind:userType="'doctor'" />
      </div>
      <div 
        class="sector flex-column-items-centered"
        v-if="this.stage == 'hasDoctor'"
      >
        <label> Wybrany doktor - {{ `${this.doctorInfo["first_name"]} ${this.doctorInfo["second_name"]} ${this.doctorInfo["last_name"]}`}}</label>
        <label> Wyszukaj Pacjenta </label>
        <SearchUser v-bind:searchUser="searchPatient" v-bind:userType="'patient'" />
      </div>
      <div 
        class="sector flex-column-items-centered"
        v-if="this.stage == 'assigned'"
      >
        <label> Sukces! Przyisano pacjenta do doktora. </label>
        <label> Wybrany doktor - {{ `${this.doctorInfo["first_name"]} ${this.doctorInfo["second_name"]} ${this.doctorInfo["last_name"]}`}}</label>
        <label> Wybrany pacjent - {{ `${this.patientInfo["first_name"]} ${this.patientInfo["second_name"]} ${this.patientInfo["last_name"]}`}}</label>
        <div class="flex-row-items-centered">
          <input
            class="input-element-standard input-element-addon spacer"
            type="button"
            value="Przypisz nowego pacjenta do tego samego doktora"
            @click="newPatientSameDoctor"
          />
          <input
            class="input-element-standard input-element-addon"
            type="button"
            value="Przypisz nowego pacjenta do nowego doktora"
            @click="newPatientNewDoctor"
          />
        </div>
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
