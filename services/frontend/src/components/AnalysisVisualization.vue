<template>
  <div class="sector flex-column-items-centered card">

    <v-row >
        <v-col>
          <v-card class="card" elevation="2">
            <v-card-title>Dane pacjenta </v-card-title>
            <v-card-text>
              <div>Pesel: {{ currentPatient.pesel }}</div>
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
              <div>Średni % próbek: {{ average }}</div>
              <div>Liczba próbek powyżej 80%: {{ counts.above }}</div>
              <div><AnalysisDownloadButton v-bind:recordingId="recordingId" v-bind:text="'Pobierz nagranie'"/></div>
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
import AnalysisDownloadButton from "./AnalysisDownloadButton.vue";


use([
  CanvasRenderer,
  BarChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent
]);

export default {
  name: 'AnalysisVisualization',
  props: ['analysisData', 'patient', 'recordingId'],
  components: {
    VChart,
    AnalysisDownloadButton
  },
  provide: {
    [THEME_KEY]: "dark",

  },
  methods: {

  },
  computed: {
    option() {
      let xAxis = Array.from({length: this.analysisData.len}, (_, i) => (i + 1)/100.0);
      return {
        tooltip: {},
        legend: {},
        xAxis: {
          data: xAxis
        },
        yAxis: {},
        series: [{
          name: 'analiza',
          type: 'bar',
          data: this.analysisData
        }]
      }
    },
    average() {
      let sum = this.analysisData.reduce((a, b) => a + b, 0);
      let avg = (sum / this.analysisData.length) || 0;
      return Math.round(avg * 100);
    },
    counts() {
        return  this.analysisData.reduce(function(s, n) {
         s[n <= 0.80 ? 'below' : 'above'] += 1;
        return s;
      }, { above: 0, below: 0 });
    },
    currentPatient() {
      return this.patient
    }
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