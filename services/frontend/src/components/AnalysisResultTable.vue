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
        >
          <td>{{analysis.status}}</td>
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
export default {
  name: 'analysisResultTable',
  props: ['analyses', 'loading'],
  data() {
    console.log(this.analyses)
    return {
    }
  },
  methods: {
    formatDate (datestr) {
      
      let date = new Date(Date.parse(datestr));
      return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()} ${date.getHours()}:${date.getMinutes() < 10 ? '0' + date.getMinutes(): date.getMinutes()}`
    },
    goToAnalysis(id) {
      this.$router.push(`/doctor/analysis/${id}`)
    }
  },
  computed: {
    load() {
      return this.loading
    }
  }

}
</script>

<style scoped>
</style>
