<template>
  <v-form
    ref="form"
    v-model="valid"
    @submit="
      (e) => {
        e.preventDefault();
        updateNews();
      }
    "
  >
    <div v-if="addingNewsDone">
      <h1>Aktualizacja przebiegła pomyślnie</h1>
      <v-divider />
    </div>
    <h1 v-if="addingNewsError">Problem ze zmianą aktualności</h1>
    <h2 v-else>Zmiany w aktualności</h2>
    <v-text-field v-model="title" :rules="rules.required" label="Tytuł" />
    <v-textarea
      solo
      v-model="description"
      :rules="rules.required"
      label="Opis"
    />
    <v-btn v-bind:disabled="!valid" color="success" class="mr-4" type="submit">
      Aktualizuj
    </v-btn>
  </v-form>
</template>

<script>
import { api } from "@/api";

export default {
  name: "UpdateNewsForm",
  props: ["newsId"],
  data() {
    return {
      title: null,
      description: null,
      addingNewsDone: false,
      addingNewsError: false,
      valid: false,
      rules: {
        required: [(v) => !!v || "Wymagane pole"],
      },
    };
  },
  beforeMount() {
    this.$store.commit("resetRegistration");
    this.getSingleNewsData();
  },
  methods: {
    async getSingleNewsData() {
      try {
        const news = await api.getNewsById(this.newsId);
        this.title = news.data.title;
        this.description = news.data.description;
      } catch (e) {
        await this.$store.dispatch("actionCheckApiError", e);
        this.$store.commit("openSnackBar", "Problem z pobieraniem danych");
        if (!this.$store.getters["isLoggenIn"]) {
          this.$router.push("/login");
        }
      }
    },
    async updateNews() {
      let payload = {
        title: this.title,
        description: this.description,
      };

      try {
        await api.updateNewsById(
          this.$store.getters["token"],
          this.newsId,
          payload
        );
        this.addingNewsDone = true;
        this.addingNewsError = false;
      } catch (e) {
        this.addingNewsDone = false;
        this.addingNewsError = true;
        await this.$store.dispatch("actionCheckApiError", e);
        this.$store.commit("openSnackBar", "Problem z wysyłaniem danych");
        if (!this.$store.getters["isLoggedIn"]) {
          this.$router.push("/login");
        }
      }
      this.$router.push(`/admin/news/`);
    },
  },
};
</script>

<style scoped>
.register-user-box {
  padding-block: 2vw;
  padding-inline: 2.5vw;
  font-size: 2vw;
}
</style>