<template>
  <div class="sector flex-column-items-centered card">

    <div class="flex-row-items-centered" style="margin-block-end: 30px">

      <table style="margin-inline-end: 30px">
        <tr>
          <td>Pesel </td>
          <td>2137 </td>
        </tr>
        <tr>
      <td>Imie</td>
      <td>Daniel</td>
        </tr>
        <tr>
            <td>Nazwisko</td>
      <td>Lipniacki </td>
        </tr>
      </table>
      <table>
        <tr>
          <td>Średni %</td>
          <td>{{ average }}</td>
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
    [THEME_KEY]: "dark"
  },
  data() {
    return {
      results: [],
      len: 0,
      average: 0,
      counts: 0, 
      option: {
        tooltip: {},
        legend: {},
        xAxis: {
          data: 0
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
  methods: {
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
  },
  mounted() {
    // await this.$store.dispatch("getAnalysisResults")
    this.results = this.$store.getters.getAnalysisResult;
    this.len = this.results.length;
    this.average = Math.round(this.getAverage() * 100) / 100;
    this.counts = this.getCounts();
    this.option.series[0].data = this.results;
    this.option.xAxis.data = Array.from({length: this.len}, (_, i) => (i + 1)/100.0);
  }
}
</script>

<style scoped>

.chart {
  width: 100%;
  height: 500px;
}

.card {
  margin: 50px;
  width: 75%;
}


</style>