<template>
  <div>
    <h1>Nagrania</h1>
    <v-divider/>
    <PatientTable :loading="loading" v-bind:patientData="patientData" />
    <RecordingsTable :loading="loading" v-bind:recordings="recordings" />
  </div>
</template>

<script>
import PatientTable from "../../components/PatientTable.vue";
import RecordingsTable from "../../components/RecordingsTable.vue";
import { api } from "@/api";

export default {
  name: "PatientData",
  components: {
    PatientTable,
    RecordingsTable,
  },
  data() {
    return {
      patientData: {},
      recordings: [],
      loading: true, 
    };
  },
  methods: {
    async getUserData(id) {
      // fetch user data
      try {
        const responeUser = await api.getUser(this.$store.getters["token"], id);
        this.patientData = responeUser.data;
      } catch (e) {
        this.$store.dispatch("actionCheckApiError", e);
        this.$store.commit("openSnackbar", "Problem z pobieraniem danych pacjneta ");
      }
      // fetch recordings
      try {
        const responeRec = await api.getRecordings(
          this.$store.getters["token"],
          id
        );
        this.recordings = responeRec.data;
      } catch (e) {
        this.$store.dispatch("actionCheckApiError", e);
        this.$store.commit(
          "openSnackbar",
          "Problem z pobieraniem danych"
        );
      }
      this.loading = false;
    },
  },
  beforeMount() {
    this.getUserData(this.$route.params.id);
  },
};
</script>

<style>
</style>