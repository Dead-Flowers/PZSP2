<template>
  <div class="analysis-table-box">
    <v-simple-table :loading=load >
      <thead>
        <tr>
          <th>Status</th>
          <th>Data badania</th>
          <th>Nazwa pliku</th>
          <th>Wynik analizy</th>
        </tr>  
      </thead>
      <tbody>
        <tr 
          v-bind:key="analysis.id" 
          v-for="analysis in analyses"
          :class="analysis.status == 'PENDING'? 'pending': ''"
        >
          <td :style="analysis.status == 'PENDING'? 'color: red': ''" >{{analysis.status}}</td>
          <td>{{ formatDate(analysis.created_date)}}</td>
          <td>{{ analysis.recording_name }}</td>
          <td>
            <v-btn @click="goToAnalysis(analysis.id)">
              Kliknij by zobaczyć wyniki 🗃️
            </v-btn>
          </td>
        </tr>
      </tbody>
    </v-simple-table>
  </div>
</template>

<script>
const stringPadding =(value, paddingSize, paddingValue) => {
  return `${value}`.padStart(paddingSize, paddingValue)
}
export default {
  name: 'analysisResultTable',
  props: ['analyses', 'loading'],
  data() {
    return {
    }
  },
  methods: {
    formatDate (datestr) {
      let date = new Date(Date.parse(datestr));
      return `${date.getFullYear()}-${stringPadding(date.getMonth()+1, 2, '0')}-${date.getDate()} ${date.getHours()}:${stringPadding(date.getMinutes(), 2, '0')}`
    },
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
