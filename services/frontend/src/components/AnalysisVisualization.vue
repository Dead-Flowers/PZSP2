<template>
  <div class="sector flex-column-items-centered card">
    <v-row>
      <v-col>
        <v-card class="card" elevation="2">
          <v-card-title>Dane pacjenta </v-card-title>
          <v-card-text>
            <div>Pesel: {{ currentPatient.pesel }}</div>
            <div>Imie: {{ currentPatient.first_name }}</div>
            <div v-if="currentPatient.second_name != null">
              Drugie imie: {{ currentPatient.second_name }}
            </div>
            <div>Nazwisko: {{ currentPatient.last_name }}</div>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col>
        <v-card class="card" elevation="2">
          <v-card-title>Dane analizy </v-card-title>
          <v-card-text>
            <div>
              <AnalysisDownloadButton
                v-bind:recordingId="recordingId"
                v-bind:text="'Pobierz nagranie'"
              />
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-row>
      <v-chart class="chart" autoresize :option="option" />
    </v-row>
    <v-row>
      <v-col>
        <v-card class="card" elevation="2" >
            <v-card-title>Statystki analizy </v-card-title>
            <v-card-text>
              <div>Średni % próbek: {{ average }}</div>
              <div>Liczba próbek powyżej 80%: {{ counts.above }}</div>
              <div>Percent of bowel sounds followed by another bowel sound within 100 ms: {{ analysisStats.percent_of_bowel_sounds_followed_by_another_bowel_sound_within_100_ms }} </div>
              <div>Percent of bowel sounds followed by another bowel sound within 200 ms: {{ analysisStats.percent_of_bowel_sounds_followed_by_another_bowel_sound_within_200_ms }} </div>
              <div>Percent of bowel sounds followed by another bowel sound within 50 ms: {{ analysisStats.percent_of_bowel_sounds_followed_by_another_bowel_sound_within_50_ms }} </div>
              <div>Bowel sounds identified total count: {{ analysisStats.bowel_sounds_identified_total_count }} </div>
              <div>Bowel sounds per minute 1st decile: {{ analysisStats.bowel_sounds_per_minute_1st_decile }} </div>
              <div>Bowel sounds per minute 1st quartile: {{ analysisStats.bowel_sounds_per_minute_1st_quartile }} </div>
              <div>Bowel sounds per minute 3rd quartile: {{ analysisStats.bowel_sounds_per_minute_3rd_quartile }} </div>
              <div>Bowel sounds per minute 9th decile: {{ analysisStats.bowel_sounds_per_minute_9th_decile }} </div>
              <div>Bowel sounds per minute maximum: {{ analysisStats.bowel_sounds_per_minute_maximum }} </div>
              <div>Bowel sounds per minute mean: {{ analysisStats.bowel_sounds_per_minute_mean }} </div>
              <div>Bowel sounds per minute median: {{ analysisStats.bowel_sounds_per_minute_median }} </div>
              <div>Bowel sounds per minute minimum: {{ analysisStats.bowel_sounds_per_minute_minimum }} </div>
              <div>Bowel sounds per minute standard deviation: {{ analysisStats.bowel_sounds_per_minute_standard_deviation }} </div>
              <div>Bowel sounds per minute total: {{ analysisStats.bowel_sounds_per_minute_total }} </div>
              <div>Frequency analysis in three minute periods: {{ analysisStats.frequency_analysis_in_three_minute_periods }} </div>
              <div>Recording length hours minutes seconds: {{ analysisStats.recording_length_hours_minutes_seconds }} </div>
              <div>Recording length minutes: {{ analysisStats.recording_length_minutes }} </div>
            </v-card-text>
        </v-card>
      </v-col>
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
  LegendComponent,
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";
import AnalysisDownloadButton from "./AnalysisDownloadButton.vue";

use([
  CanvasRenderer,
  BarChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
]);

export default {
  name: "AnalysisVisualization",
  props: ["analysisStats", "analysisData", "patient", "recordingId"],
  components: {
    VChart,
    AnalysisDownloadButton,
  },
  provide: {
    [THEME_KEY]: "dark",
  },
  methods: {},
  computed: {
    option() {
      const numPoints = this.analysisData.length;
      let xAxis = Array.from(
        { length: numPoints },
        (_, i) => (i + 1) / 100.0
      );
      return {
        tooltip: {},
        legend: {},
        xAxis: {
          data: xAxis,
          name: "Czas [s]",
          axisTick: {
            show: true,
            alignWithLabel: true
          },
          axisLabel: {
            rotate: 90,
            hideOverlap: true,
            interval: (index, value) => value % 5 == 0
          }
        },
        yAxis: {
          name: "Prawdopodobieństwo"
        },
        series: [
          {
            name: "Analiza prawdopodobieństwa",
            type: "bar",
            data: this.analysisData,
          },
        ],
      };
    },
    average() {
      let sum = this.analysisData.reduce((a, b) => a + b, 0);
      let avg = sum / this.analysisData.length || 0;
      return Math.round(avg * 100);
    },
    counts() {
      return this.analysisData.reduce(
        function (s, n) {
          s[n <= 0.8 ? "below" : "above"] += 1;
          return s;
        },
        { above: 0, below: 0 }
      );
    },
    currentPatient() {
      return this.patient;
    },
  },
};
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