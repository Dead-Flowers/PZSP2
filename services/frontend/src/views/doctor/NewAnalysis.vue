<template>
  <div>
    <h1>Nowa analiza</h1>
    <h2>
      {{
        `${this.patientData["first_name"]} ${this.patientData["second_name"]} ${this.patientData["last_name"]}`
      }}
    </h2>
    <AnalysisInit v-bind:patientID="chosenUserId" />
  </div>
</template>

<script>
import AnalysisInit from "../../components/AnalysisInit.vue";
import { api } from "@/api";

export default {
  name: "NewAnalysis",
  components: {
    AnalysisInit,
  },
  data() {
    return {
      patientData: {},
      chosenUserId: null,
    };
  },
  methods: {
    async getUserData(id) {
      // fetch user data
      try {
        const patient = await api.getUser(this.$store.getters["token"], id);
        this.patientData = patient.data;
      } catch (e) {
        this.$store.dispatch("actionCheckApiError", e);
        this.$store.commit("openSnackbar", "Problem z pobieraniem danych pacjneta ");
      }
      // fetch analysis
      try {
        const analyses = await api.getAnalysis(
          this.$store.getters["token"],
          id
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
    },
  },
  beforeMount() {
    this.chosenUserId = this.$route.params.id;
    this.getUserData(this.chosenUserId);
  },
};
</script>

<style>
</style>
