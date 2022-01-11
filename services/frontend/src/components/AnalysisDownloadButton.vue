<template>
    <v-btn @click="downloadRecording()"><v-icon>mdi-download</v-icon>{{ isDownloading ? `${downloadPercentage}%` : text }} </v-btn>
</template>
<script>
import { api } from "@/api";
import { saveRecording } from "@/utils";
export default {
    props: ['recordingId', 'recordingName', 'text'],
    data() {
        return {
            isDownloading: false,
            downloadPercentage: '0'
        }
    },
    methods: {
        async downloadRecording() {
        if (!this.recordingId) {
            this.$store.commit("openSnackbar", "Nie znaleziono nagrania");
            return;
        }
        const { data: { filename } } = await api.getRecording(this.$store.getters['token'], this.recordingId); 
        this.isDownloading = true;
        this.downloadPercentage = 0;
        api.downloadRecording(this.$store.getters["token"], this.recordingId, this.downloadProgressUpdate)
            .then(data => saveRecording(data, filename)).finally(() => this.isDownloading = false);
        },
        downloadProgressUpdate(event) {
            const total = parseFloat(event.total) + 0.01;
            const current = event.loaded;
            this.downloadPercentage = Math.floor(current / total * 100);
        }
    }

};
</script>
