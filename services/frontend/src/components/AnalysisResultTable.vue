<template>
  <div class="analysis-table-box">
    <table> 
      <tr>
        <th @click="sortBy('status')">Status</th>
        <th @click="sortBy('created_date')">Data badania</th>
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
      lastSortingCriteria: null,
    }
  },
  methods: {
    sortBy(criteria) {
      let direction = (criteria == this.lastSortingCriteria)? -1 : 1;
      this.analysis.sort((a, b) => (a[criteria] >= b[criteria]) ? direction *  1 : direction * -1);
      if (direction == 1) this.lastSortingCriteria = criteria;
      else this.lastSortingCriteria = null;
    },

    sortByMultiple(criteria) {
      let criteria_cmpr = criteria.toString();
      let direction = (criteria_cmpr == this.lastSortingCriteria)? -1 : 1;
      this.analysis.sort((a, b) => (this.combineRecords(a, criteria) >= this.combineRecords(b, criteria)) ? direction * 1 :  direction * -1);
      if (direction == 1) this.lastSortingCriteria = criteria_cmpr;
      else this.lastSortingCriteria = null;
    },
    combineRecords(d, criteria) {
      let s = "";
      criteria.forEach(element => {
        s += d[element];
      });
      return s;    
    },
    formatDate (datestr) {
      let date = new Date(Date.parse(datestr));
      return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()} ${date.getHours()}:${date.getMinutes()}`
    },
  },

}
</script>

<style scoped>
.analysis-table-box {
  background-color: var(--color-sector);
  padding-block: 2vw;
  padding-inline: 2.5vw;
  display: table;
  color: var(--color-text);
}
</style>
