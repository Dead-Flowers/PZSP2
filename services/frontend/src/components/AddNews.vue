<template>
  <v-form
    ref="form"
    v-model="valid"
    @submit="
      (e) => {
        e.preventDefault();
        submitNews();
      }
    "
  >
    <div v-if="addingNewsDone">
      <h1>Poprawnie dodano aktualność</h1>
      <v-divider />
    </div>
    <h1 v-if="addingNewsError">Problem z dodaniem aktualności</h1>
    <h2 v-else>Dodawanie nowej aktualności</h2>
    <v-text-field v-model="title" :rules="rules.required" label="Tytuł" />
    <v-textarea
      solo
      v-model="description"
      :rules="rules.required"
      label="Opis"
      row="2"
    />
    <v-btn v-bind:disabled="!valid" color="success" class="mr-4" type="submit">
      Dodaj
    </v-btn>
  </v-form>
</template>

<script>
import { api } from "@/api";

export default {
  name: "AddNewsForm",
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
  },
  methods: {
    async submitNews() {
      let payload = {
        title: this.title,
        description: this.description,
      };
      try {
        await api.addNews(this.$store.getters["token"], payload);
        this.addingNewsError = false;
        this.addingNewsDone = true;
      } catch (e) {
        this.addingNewsError = true;
        this.addingNewsDone = false;
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