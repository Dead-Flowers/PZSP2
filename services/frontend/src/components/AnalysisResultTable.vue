<template>
  <div>
    <table class="patientData"> 
      <tr>
        <th>Pesel/Nr Paszportu</th>
        <th>Imię</th>
        <th>Nazwisko</th>
        <th>Wynik analizy</th>
      </tr>  
      {}
    </table>
  </div>
</template>

<script>
export default {
  name: 'AnalysisResultTable',
  
}
</script>

<style>
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

.tableRecordEven {
  background-color: var(--color-table-record1);
}

.tableRecordOdd {
  background-color: var(--color-table-record2);
}
</style>
