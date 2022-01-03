<template>
  <div v-if="analysisStarted" class="sector flex-column-items-centered card"> Rozpocznij analizę </div>

  <div v-else class="sector flex-column-items-centered card">

    <v-row >
        <v-col>
          <v-card class="card" elevation="2">
            <v-card-title>Dane pacjenta </v-card-title>
            <v-card-text>
              <div>Pesel: {{ currentPatient.patientId }}</div>
              <div>Imie: {{ currentPatient.first_name }}</div>
              <div v-if="currentPatient.second_name != null">Drugie imie: {{ currentPatient.second_name }}</div>
              <div>Nazwisko: {{ currentPatient.last_name }} </div>
            </v-card-text> 
          </v-card>
        </v-col>

        <v-col>
          <v-card class="card" elevation="2">
            <v-card-title>Dane analizy </v-card-title>
            <v-card-text>
              <div>Średni % {{ average }}</div>
              <div>Powyżej 80%: {{ counts.above }}</div>
            </v-card-text> 
          </v-card>
        </v-col>
    </v-row>


    <v-row>
      <v-chart class="chart" 
      autoresize
      :option="option" />
    </v-row>
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
    [THEME_KEY]: "dark",

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
  height: 50vh;
}

.card {
  height: 100%;
}


</style>