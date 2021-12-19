<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <Navbar v-bind:usertype="'admin'" />
    <div class="flex-row-items-centered">
      <div class="sector flex-column-items-centered">
        <label> Wyszukaj Pacjenta </label>
        <SearchPatient v-bind:searchUser="searchPatient" v-bind:usertype="'patient'" />
      </div>
      <div class="sector flex-column-items-centered">
        <label> Wyszukaj Doktora </label>
        <SearchPatient v-bind:searchUser="searchDoctor" v-bind:usertype="'doctor'" />
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
import SearchPatient from '../../components/SearchUser.vue'
import { api } from '@/api';

export default {
  name: 'AssignDoctorToPatient',
  components: {
    Navbar,
    SearchPatient,
  },
  data() {
    return {
      patientId: null,
      doctorId: null
    }
  },
  methods: {
    searchPatient(patientId) {
      this.patientId = patientId
      console.log(patientId);
      // do sth with backend
    },
    searchDoctor(userId) {
      this.doctorId = userId
      console.log(userId);
      // do sth with backend
    },
    async assignD2P() {
      console.log(this.patientId)
      console.log(this.doctorId)
      let newData = {
        doctor_id: this.doctorId
      }
      //TODO catch errro
      const response = await api.updateUser(this.$store.getters["token"], this.patientId, newData)

      console.log(response);
    },
  }
}
</script>

<style scoped>
label {
  font-size: 2rem;
  padding: 5px;
  margin-block-start: 30px;
}

</style>
