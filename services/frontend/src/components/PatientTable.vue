<template>
  <div class="patient-data-table">
    <table> 
      <tr>
        <th>Pesel/Nr Paszportu</th>
        <td class="table-record-even">{{patientData.patientId}}</td>
      </tr>
      <tr>
        <th>Imię</th>
        <td class="table-record-odd">{{'' + patientData.firstName + ' ' + patientData.secondName}}</td>
      </tr>
      <tr>  
        <th>Nazwisko</th>
        <td class="table-record-even">{{patientData.surname}}</td>
      </tr>
      <tr>
        <th>Data ostatniego badania</th>
        <td class="table-record-odd">{{patientData.lastLab}}</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'PatientTable',
  props: ['patientData'],
}
</script>

<style scoped>
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
  filter: brightness(90%);
}
</style>
