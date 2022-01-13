<template>
  <div class="news-table-box">
    <v-btn @click="createNew()"> <v-icon>mdi-plus</v-icon> Dodaj </v-btn>
    <v-simple-table :loading="load">
      <thead>
        <tr>
          <th>Tytuł</th>
          <th>Data dodania</th>
        </tr>
      </thead>
      <tbody>
        <tr v-bind:key="singleNews.id" v-for="singleNews in news">
          <td>{{ singleNews.title }}</td>
          <td>{{ formatDate(singleNews.creation_date) }}</td>
          <td>
            <v-btn @click="goToNews(singleNews.id)">
              <v-icon>mdi-note-search</v-icon> Edytuj
            </v-btn>
            <v-btn @click="removeNews(singleNews.id)">
              <v-icon>mdi-delete</v-icon> Usuń
            </v-btn>
          </td>
        </tr>
      </tbody>
    </v-simple-table>
  </div>
</template>

<script>
import { formatDate } from "../utils";
import { api } from "@/api";

export default {
  name: "newsResultTable",
  props: ["loading"],
  data() {
    return {
      news: [],
    };
  },
  methods: {
    async getNewsData() {
      try {
        const news = await api.getNews({});
        console.log(news.data);
        this.news = news.data;
      } catch (e) {
        this.$store.dispatch("actionCheckApiError", e);
        this.$store.commit("openSnackBar", "Problem z pobieraniem danych");
      }
    },
    formatDate,
    goToNews(id) {
      this.$router.push(`/admin/news/edit/${id}`);
    },
    async removeNews(id) {
      const choice = window.confirm(
        "Na pewno chcesz usunąć wybraną aktualność?"
      );
      if (!choice) return;
      await this.$store.dispatch("actionRemoveNews", id);
      await this.getNewsData();
    },
    createNew() {
      this.$router.push("/admin/news/new");
    },
  },
  computed: {
    load() {
      return this.loading;
    },
  },
  beforeMount() {
    this.getNewsData();
  },
};
</script>

<style scoped>
.pending {
  animation: color-change 4s infinite;
}

@keyframes color-change {
  0% {
    background-color: #00ccff;
  }
  50% {
    background-color: transparent;
  }
  100% {
    background-color: #00ccff;
  }
}
</style>
