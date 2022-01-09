<template>
  <div class="analysis-table-box">
    <v-simple-table>
      <thead>
        <tr>
          <th>Data stworzenia</th>
          <th>Nazwa pliku</th>
          <th>Analizy dla tego pliku</th>
          <th>Ponowna analiza</th>
        </tr>  
      </thead>
      <tbody>
        <tr 
          v-bind:key="recording.id" 
          v-for="recording in recordings"
        >
          <td>{{formatDate(recording.creation_date)}}</td>
          <td>{{ recording.filename }}</td>
          <td>
            <router-link :to="`/doctor/analysis/${recording.recording_id}`" >
              Kliknij by zobaczyć analizy dla tego pliki 🗃️ TODO
            </router-link>
          <td>
            <a  @click="startAnalysis(recording.id)" >
              Zrób ponownie analiza dla tego pliku 🗃️
            </a>
          </td>
        </tr>
      </tbody>
    </v-simple-table>
  </div>
</template>

<script>
import { api } from '@/api';

export default {
  name: 'recordingsTable',
  props: ['recordings'],
  data() {
    console.log(this.analyses)
    return {
    }
  },
  methods: {
    formatDate (datestr) {
      let date = new Date(Date.parse(datestr));
      return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()} ${date.getHours()}:${date.getMinutes()}`
    },
    async startAnalysis(id) {
        console.log("tak")
        let response = api.startAnalysis(this.$store.getters["token"], id)
        this.$store.commit("setAnalysisID", response.data)
        this.$router.push("/doctor/analysisStarted")
    }
  },

}
</script>

<style scoped>
</style>