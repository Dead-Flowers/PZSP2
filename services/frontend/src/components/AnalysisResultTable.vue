<template>
  <div class="analysis-table-box">
    <v-simple-table :loading=load >
      <thead>
        <tr>
          <th>Status</th>
          <th>Data badania</th>
          <th>Nagranie</th>
          <th>Wynik analizy</th>
        </tr>  
      </thead>
      <tbody>
        <tr 
          v-bind:key="analysis.id" 
          v-for="analysis in analyses"
          :class="analysis.status == 'PENDING'? 'pending': ''"
        >
          <td>{{analysis.status}}</td>
          <td>{{ formatDate(analysis.created_date)}}</td>
          <td>
            <div>
              <span>{{ analysis.recording_name }}</span>
            </div>
          </td>
          <td>
            <v-btn @click="goToAnalysis(analysis.id)">
              <v-icon>mdi-note-search</v-icon> Pokaż wyniki
            </v-btn>
          </td>
        </tr>
      </tbody>
    </v-simple-table>
  </div>
</template>

<script>
import { formatDate } from "../utils";

export default {
  name: 'analysisResultTable',
  props: ['analyses', 'loading'],
  data() {
    return {
    }
  },
  methods: {
    formatDate,
    goToAnalysis(id) {
      this.$router.push(`/${this.$store.getters["userType"]}/analysis/${id}`)
    }
  },
  computed: {
    load() {
      return this.loading
    }
  },
  
}
</script>

<style scoped>
.pending {
  animation: color-change 4s infinite;
}

@keyframes color-change {
  0% { background-color: #00ccff; }
  50% { background-color: transparent; }
  100% { background-color: #00ccff; }
}
</style>
