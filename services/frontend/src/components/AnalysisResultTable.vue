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
        v-bind:class="{'table-record-even': index % 2 === 0, 'table-record-odd': index % 2 === 1 }"  
        v-for="(record, index) in analysisData"
      >
        <td>{{record.analysisId}}</td>
        <td>{{'' + record.patientId + ' ' + record.patientIdType}}</td>
        <td>{{record.patientName}}</td>
        <td>{{record.patientSurname}}</td>
        <td>{{record.date}}</td>
        <td>
          <a class="link" v-bind:href="record.analysisHyperlink">
            Kliknij by pobrać wynik 🗃️
          </a>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'AnalysisResultTable',
  props: ['analysisData']
}
</script>

<style scoped>
.analysis-table-box {
  background-color: var(--color-sector);
  border-radius: 3px;
  padding-block: 40px;
  padding-inline: 50px;
  width: -webkit-fit-content;
  height: -webkit-fit-content;
  width: -moz-fit-content;
  height: -moz-fit-content;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  font-family: "Balsamiq Sans", cursive;
  color: var(--color-text);
}
table {
  width: 100%;
  min-width: 400px;
  margin: 30px auto 0 auto;
}

th {
  border: none;
  background-color: var(--color-table-header);
  color: white;
  text-transform: uppercase;
  padding: 10px;
}
  
tr, td {
  border: none;
  padding: 5px;
  color: var(--color-text);
}

.table-record-even {
  background-color: var(--color-table-record1);
}

.table-record-odd {
  background-color: var(--color-table-record2);
}

.link {
  background-color: transparent !important;
  text-decoration: none;
  font-size: 0.8rem !important;
  color: var(--color-text);
}

.link:hover {
  filter: brightness(95%);
}
</style>
