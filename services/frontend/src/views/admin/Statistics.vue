<template>
  <div class="sector flex-column-items-centered card">
      <v-row>
          <v-col>
            <v-card :loading="loading" class="card" elevation="2" >
                <v-card-title>Statystyki analiz </v-card-title>
                <v-card-text>
                    <div> Liczba analiz zakończonych sukcesem: {{ stats.success }} </div>
                    <div> Liczba analiz zakończonych niepowodzeniem: {{ stats.failure }} </div>
                    <div v-if="stats.exceptions.length != 0"> Błędy w analizach:  </div>
                    <div  v-bind:key="err" v-for="err in stats.exceptions"> * {{ err }} </div>
                </v-card-text>
            </v-card>
          </v-col> 
      </v-row>
  </div>
</template>

<script>
import { api } from '@/api'

export default {
  name: 'Statistics',
  data() {
      return {
          loading: true,
          stats: {
            success: 0,
            failure: 0,
            exceptions: []
          },
          status: "Not checked yet",
      }
  },
  mounted() {
    this.getStats()
  },
  methods: {
      async getStats() {
        try {
            this.loading = true
            const st = await api.getStatistics(this.$store.getters["token"])
            this.stats = st.data
            this.loading = false
        } catch(e) {
          this.$store.dispatch("actionCheckApiError", e);
          if (!this.$store.getters["isLoggedIn"]) {
            this.$router.push("/login");
          }
          this.$store.commit("openSnackbar", "Wystąpił błąd podczas pobierania statystk");
        }
      },
  }
}
</script>

<style>

</style>