<template>
  <div class="analysis-table-box">
    <v-simple-table>
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
        >
          <td>{{analysis.status}}</td>
          <td>{{ formatDate(analysis.created_date)}}</td>
          <td>
            <router-link :to="`/doctor/analysis/${analysis.recording_id}`" >
              Kliknij by zobaczyć nagranie 🗃️
            </router-link>
          <td>
            <router-link :to="`/doctor/analysis/${analysis.id}`" >
              Kliknij by zobaczyć wyniki 🗃️
            </router-link>
          </td>
        </tr>
      </tbody>
    </v-simple-table>
  </div>
</template>

<script>
export default {
  name: 'analysisResultTable',
  props: ['analyses'],
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
  },

}
</script>

<style scoped>
</style>
