<template>
  <div class="analysis-table-box">
    <table> 
      <tr>
        <th>Numer analizy</th>
        <th>Pesel/Nr Paszportu</th>
        <th>Imię</th>
        <th>Nazwisko</th>
        <th>Data badania</th>
        <th>Wynik analizy</th>
      </tr>  
      <tr 
        v-bind:key="record.analysisId" 
        v-for="record in analyses"
      >
        <td>{{record.analysisId}}</td>
        <td>{{ `${record.patientId} ${record.patientIdType}` }}</td>
        <td>{{record.patientName}}</td>
        <td>{{record.patientSurname}}</td>
        <td>{{record.date}}</td>
        <td>
          <router-link to="/analysis-view" v-bind:href="record.analysisHyperlink">
            Kliknij by pobrać wynik 🗃️
          </router-link>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'AnalysisResultTable',
  props: ['analyses']
}
</script>

<style scoped>
.analysis-table-box {
  background-color: var(--color-sector);
  padding-block: 40px;
  padding-inline: 50px;
  display: table;
  color: var(--color-text);
}
</style>
