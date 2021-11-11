<template>
  <div class="patient-data-table">
    <table> 
      <tr>
        <th>Pesel/Nr Paszportu</th>
        <td class="table-record-even">{{patientData.patientId}}</td>
      </tr>
      <tr>
        <th>Imię</th>
        <td class="table-record-odd">{{`${patientData.firstName} ${patientData.secondName}`}}</td>
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

</style>
