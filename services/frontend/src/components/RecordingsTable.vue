<template>
  <div class="analysis-table-box">
    <v-simple-table>
      <thead>
        <tr>
          <th>Data stworzenia</th>
          <th>Nazwa pliku</th>
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
            <v-btn @click="startAnalysis(recording.id)">
              Kliknij by przeprowadzić poniwnie analize 🗃️
            </v-btn>
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
      return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()} ${date.getHours()}:${date.getMinutes() < 10 ? '0' + date.getMinutes(): date.getMinutes()}`
    },
    async startAnalysis(id) {
        let response = await api.startAnalysis(this.$store.getters["token"], id)
        this.$router.push(`/doctor/analysisStarted/${response.data}`)
    }
  },

}
</script>

<style scoped>
</style>