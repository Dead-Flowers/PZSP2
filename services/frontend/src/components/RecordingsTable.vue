<template>
  <div class="analysis-table-box">
    <v-simple-table>
      <thead>
        <tr>
          <th>Data stworzenia</th>
          <th>Nazwa pliku</th>
          <th>Pobierz</th>
          <th>Ponowna analiza</th>
        </tr>  
      </thead>
      <tbody>
        <tr 
          v-bind:key="recording.id" 
          v-for="recording in recordings"
        >
          <td>{{formatDate(recording.creation_date)}}</td>
          <td>
            {{ recording.filename }}
          </td>
          <td>
             <AnalysisDownloadButton v-bind:recordingId="recording.id" v-bind:text="''"/>
          </td>
          <td>
            <v-btn @click="startAnalysis(recording.id)">
              <v-icon>mdi-refresh</v-icon>
            </v-btn>
          </td>
        </tr>
      </tbody>
    </v-simple-table>
  </div>
</template>

<script>
import { api } from '@/api';
import { formatDate } from "../utils";
import AnalysisDownloadButton from "./AnalysisDownloadButton.vue";

export default {
  name: 'recordingsTable',
  props: ['recordings'],
  components: {
    AnalysisDownloadButton
  },
  data() {
    console.log(this.analyses)
    return {
    }
  },
  methods: {
    formatDate,
    async startAnalysis(id) {
        let response = await api.startAnalysis(this.$store.getters["token"], id)
        this.$router.push(`/doctor/analysisStarted/${response.data}`)
    }
  },

}
</script>

<style scoped>
</style>