<template>
  <div v-if="analysisStarted" class="sector flex-column-items-centered card"> Rozpocznij analizę </div>

  <div v-else class="sector flex-column-items-centered card">

    <div class="flex-row-items-centered" style="margin-block-end: 1.5vw">

      <table style="margin-inline-end: 1.5vw">
        <tr>
          <td>Pesel </td>
          <td>{{ currentPatient.patientId }} </td>
        </tr>
        <tr>
      <td>Drugie imie</td>
      <td>{{ currentPatient.firstName }}</td>
        </tr>
         <tr v-if="currentPatient.secondName != null">
      <td v-if="currentPatient.secondName != null" >Imie</td>
      <td v-if="currentPatient.secondName != null">{{ currentPatient.firstName }}</td>
        </tr>
        <tr>
            <td>Nazwisko</td>
      <td>{{ currentPatient.surname }} </td>
        </tr>
      </table>
      <table>
        <tr>
          <td>Średni %</td>
          <td>{{ average }}%</td>
        </tr>
        <tr>
            <td>Powyżej 80%</td>
      <td>{{ counts.above }}</td>
        </tr>
        <tr>
        </tr>
      </table>
    </div>
    <v-chart class="chart" 
    autoresize
    :option="option" />
  </div>
</template>

<script>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { BarChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";


use([
  CanvasRenderer,
  BarChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent
]);

export default {
  name: 'AnalysisVisualization',
  props: ['analysisData'],
  components: {
    VChart
  },
  provide: {
    [THEME_KEY]: "vintage"
  },
  data() {
    return {
      analysisStarted: false,
      currentPatient: {},
      results: [],
      len: 0,
      average: 0,
      counts: 0, 
      option: {
        tooltip: {},
        legend: {},
        xAxis: {
          data: []
        },
        yAxis: {},
        series: [{
          name: 'analiza',
          type: 'bar',
          data: []
        }]
      },
    }
  },
  beforMount() {
    this.analysisStarted = this.$store.getters.analysisStarted;
  },
  methods: {
    getUser() {
      console.log("patien")
      this.currentPatient = this.$store.getters.getCurrentPatient
    },
    getAverage() {
      let sum = this.results.reduce((a, b) => a + b, 0);
      let avg = (sum / this.results.length) || 0;
      return avg
    },
    getCounts() {
      return  this.results.reduce(function(s, n) {
         s[n <= 0.80 ? 'below' : 'above'] += 1;
        return s;
      }, { above: 0, below: 0 });
    },
    setData() {
      this.results = this.$store.getters.getAnalysisResult;
      this.len = this.results.length;
      this.average = Math.round(this.getAverage() * 100);
      this.counts = this.getCounts();
      this.option.series[0].data = this.results;
      this.option.xAxis.data = Array.from({length: this.len}, (_, i) => (i + 1)/100.0);
    }
  },
  async mounted() {
    await this.$store.dispatch("getAnalysisResults")
    this.setData()
    this.getUser()
  }
}
</script>

<style scoped>

.chart {
  width: 100%;
  height: 0.5vh;
}

.card {
  margin: 2.5vw;
  width: 75%;
}


</style>