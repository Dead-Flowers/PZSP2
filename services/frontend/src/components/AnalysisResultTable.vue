<template>
  <div class="analysis-table-box">
    <table> 
      <tr>
        <th @click="sortBy('analysisId')">Numer id analizy</th>
        <th @click="sortByMultiple(['patientIdType', 'patientId'])">Pesel/Nr Paszportu</th>
        <th @click="sortByMultiple(['patientFirstName', 'patientSecondName'])">Imię</th>
        <th @click="sortBy('surname')">Nazwisko</th>
        <th @click="sortBy('date')">Data badania</th>
        <th>Wynik analizy</th>
      </tr>  
      <tr 
        v-bind:key="record.analysisId" 
        v-for="record in analysis"
      >
        <td>{{record.analysisId}}</td>
        <td>{{ `${record.patientIdType} - ${record.patientId}` }}</td>
        <td>{{`${record.patientFirstName} ${record.patientSecondName}`}}</td>
        <td>{{record.patientSurname}}</td>
        <td>{{record.date}}</td>
        <td>
          <router-link to='/doctor/analysis-view' >
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
  props: ['analysis'],
  methods: {
    sortBy(criteria) {
      console.log("test")
      this.analysis.sort((a, b) => (a[criteria] > b[criteria]) ? 1 : -1);
    },
    sortByMultiple(criteria) {
      this.analysis.sort((a, b) => (this.combineRecords(a, criteria) > this.combineRecords(b, criteria)) ? 1 : -1);
    },
    combineRecords(d, criteria) {
      let s = "";
      criteria.forEach(element => {
        s += d[element];
      });
      return s;    
    }
  },
  beforeMount() {
    // this is a mock to test sorting
    this.analysis = [
      {
        analysisId: 1,
        patientIdType: "pesel",
        patientId: "01234567893",
        patientFirstName: "Jan",
        patientSecondName: "A",
        patientSurname: "Kowal",
        date: "2021-12-20"
      },
      {
        analysisId: 4,
        patientIdType: "pesel",
        patientId: "01234567891",
        patientFirstName: "Jan",
        patientSecondName: "B",
        patientSurname: "Kowal",
        date: "2021-12-21"
      },
      {
        analysisId: 3,
        patientIdType: "Id paszportu",
        patientId: "AE322B4",
        patientFirstName: "Kamil",
        patientSecondName: "Krykiet",
        patientSurname: "Pajda",
        date: "2021-11-20"
      },
    ]
  }
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
