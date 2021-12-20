<template>
  <div class="patient-data-table">
    <table> 
      <tr>
        <th>Pesel/Nr Paszportu</th>
        <td class="table-record-even">{{ ( patientData.pesel == null) ? patientData.passport_num : patientData.pesel }}</td>
      </tr>
      <tr>
        <th>Imię</th>
        <td class="table-record-odd">{{`${patientData.first_name} ${patientData.second_name}`}}</td>
      </tr>
      <tr>  
        <th>Nazwisko</th>
        <td class="table-record-even">{{patientData.last_name}}</td>
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
