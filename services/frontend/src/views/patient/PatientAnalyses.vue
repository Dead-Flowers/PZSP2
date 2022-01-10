<template>
  <div>
    <PatientTable :loading="loading" v-bind:patientData="patientData" />
    <AnalysisResultTable :loading="loading" v-bind:analyses="analyses" />
  </div>
</template>

<script>
import PatientTable from "../../components/PatientTable.vue";
import AnalysisResultTable from "../../components/AnalysisResultTable.vue";
import { api } from "@/api";

export default {
  name: "PatientData",
  components: {
    PatientTable,
    AnalysisResultTable,
  },
  data() {
    return {
      loading: true,
      patientData: {},
      analyses: [],
    };
  },
  async mounted() {
    // fetch patient data
    try {
      const responeUser = await api.getUser(
        this.$store.getters["token"],
        this.$store.getters["id"]
      );
      this.patientData = responeUser.data;
    } catch (e) {
      this.$store.dispatch("actionCheckApiError", e);
      this.$store.commit("openSnackbar", "Problem z pobieraniem danych pacjneta ");
    }
    // fetch analysis
    try {
      const responeAnal = await api.getAnalysis(
        this.$store.getters["token"],
        this.$store.getters["id"]
      );
      this.analyses = responeAnal.data;
    } catch (e) {
      this.$store.dispatch("actionCheckApiError", e);
      this.$store.commit("openSnackbar", "Problem z pobieraniem danych");
    }
    this.loading = false;
  },
};
</script>

<style>
</style>