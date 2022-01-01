<template>
  <div class="analysis-table-box">
    <table> 
      <tr>
        <th>Status</th>
        <th>Data badania</th>
        <th>Nagranie</th>
        <th>Wynik analizy</th>
      </tr>  
      <tr 
        v-bind:key="record.id" 
        v-for="record in analysis"
      >
        <td>{{record.status}}</td>
        <td>{{ formatDate(record.created_date)}}</td>
        <td>
          <router-link to='/doctor/analysis-view' >
            Kliknij by zobaczyć nagranie 🗃️
          </router-link>
        <td>
          <router-link to='/doctor/analysis-view' >
            Kliknij by zobaczyć wyniki 🗃️
          </router-link>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'AnalysisResultTable',
  props: ['analysis'],
  data() {
    return {
    }
  },
  methods: {
    formatDate (datestr) {
      let date = new Date(Date.parse(datestr));
      return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()} ${date.getHours()}:${date.getMinutes()}`
    },
  },

}
</script>

<style scoped>
</style>
