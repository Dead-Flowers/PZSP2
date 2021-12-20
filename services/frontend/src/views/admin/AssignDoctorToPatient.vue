<template>
  <div class="max-screen-space-container flex-row-items-start">
    <Navbar v-bind:usertype="'admin'" />
    <div class="navbar-as-adjacent flex-column-items-centered">
      <div  
        class="sector flex-column-items-centered"
        v-if="this.stage == 0"
      >
        <label> Wyszukaj Pacjenta </label>
        <SearchUser v-bind:searchUser="searchPatient" v-bind:userType="'patient'" />
      </div>
      <div 
        class="sector flex-column-items-centered"
        v-if="this.stage == 1"
      >
        <label> Wybrany pacjent {{ `${this.patientInfo["first_name"]} ${this.patientInfo["second_name"]} ${this.patientInfo["last_name"]}`}}</label>
        <label> Wyszukaj Doktora </label>
        <SearchUser v-bind:searchUser="searchDoctor" v-bind:userType="'doctor'" />
      </div>
      <div 
        class="sector flex-column-items-centered"
        v-if="this.stage == 2"
      >
        <label> Sukces! Przyisano pacjenta do doktora. </label>
        <label> Wybrany pacjent {{ `${this.patientInfo["first_name"]} ${this.patientInfo["second_name"]} ${this.patientInfo["last_name"]}`}}</label>
        <label> Wybrany doktor {{ `${this.patientInfo["first_name"]} ${this.patientInfo["second_name"]} ${this.patientInfo["last_name"]}`}}</label>
        <input
          class="input-element-standard input-element-addon"
          type="button"
          name="button"
          value="Przypisz nowego pacjenta do tego doktora"
          @click="searchForUser"
        />
      </div>
    </div>


    <input
      class="input-element-standard button"
      type="button"
      value="Przypisz pacjenta do doktora"
      @click="assignD2P"
    />
  </div>
</template>

<script>
import Navbar from '../../components/Navbar.vue'
import SearchUser from '../../components/SearchUser.vue'
import { api } from '@/api';

export default {
  name: 'AssignDoctorToPatient',
  components: {
    Navbar,
    SearchUser,
  },
  data() {
    return {
      patientId: null,
      patientInfo: null,
      doctorId: null,
      doctorInfo: null,
      stage: 0,
    }
  },
  methods: {
    searchPatient(patient) {
      this.patientInfo = patient;
      this.patientId = patient.id;
      this.stage = 1;
    },
    searchDoctor(user) {
      this.doctorInfo = user;
      this.doctorId = user.id;
      this.assignD2P();
      this.stage = 2;
    },
    async assignD2P() {
      let newData = {
        doctor_id: this.doctorId,
      }
      const response = await api.updateUser(this.$store.getters["token"], this.patientId, newData);
    },
    newPatientSameDoctor() {

    },
    newPatientNewDoctor() {
      this.stage = 0;
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

</style>
