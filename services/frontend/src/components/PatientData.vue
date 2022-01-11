<template>
  <div>
    <PatientTable :loading="loading" v-bind:patientData="patientData" />
    <AnalysisResultTable :loading="loading" v-bind:analyses="analyses" />
  </div>
</template>

<script>
import PatientTable from "./PatientTable.vue";
import AnalysisResultTable from "./AnalysisResultTable.vue";
import { api } from "@/api";

export default {
  name: "PatientData",
  props: ["patientId"],
  components: {
    PatientTable,
    AnalysisResultTable,
  },
  data() {
    return {
      patientData: {},
      analyses: [],
      loading: true
    };
  },
  methods: {
    async getUserData() {
      // fetch user data
      try {
        const patient = await api.getUser(this.$store.getters["token"], this.patientId);
        this.patientData = patient.data;
      } catch (e) {
        this.$store.dispatch("actionCheckApiError", e);
        this.$store.commit("openSnackbar", "Problem z pobieraniem danych pacjneta ");
      }
      // fetch analysis
      try {
        const analyses = await api.getAnalysis(
          this.$store.getters["token"],
          this.patientId
        );
        this.analyses = analyses.data;
        console.log(analyses);
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
  sockets: {
    onmessage(event) {
      // listen for changes and update existing analyses
      // if such an analysis doesn't exist, refetch all
      this.loading = true;
      const obj = JSON.parse(event.data);
      if (obj.type != "analysis-state-updated") return;
      for (let analysis of this.analyses) {
        if (analysis.id != obj.payload.id) continue;
        analysis.status = obj.payload.status;
        console.log("updated analysis status");
        this.loading = false;
        return;
      }
      console.log("analysis not found, refetching");
      this.getUserData();
    },
  },
  beforeMount() {
    this.getUserData();
  },
};
</script>

<style>
</style>
