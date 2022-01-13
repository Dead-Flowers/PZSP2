<template>
  <div style="display: flex">
    <div style="width: 40vw">
      <h1>Witaj w BowelLab</h1>
      <v-btn
        color="primary"
        elevation="2"
        large
        outlined
        @click="goToLoginPage()"
        style="margin-block: 10px"
      >
        Zaloguj się
      </v-btn>
      <v-expansion-panels accordion>
        <v-expansion-panel v-for="n in news" :key="n.id">
          <v-expansion-panel-header>{{ n.title }} </v-expansion-panel-header>
          <v-expansion-panel-content>
            {{ n.description }}
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </div>
    <img src="doctor.png" class="welcome-img" />
  </div>
</template>

<script>
import router from "../../router";
import { api } from "@/api";

export default {
  name: "Welcome",
  methods: {
    goToLoginPage() {
      router.push("/login");
    },
    async getNews() {
      try {
        const news = await api.getNews({});
        console.log(news.data);
        this.news = news.data;
      } catch (e) {
        this.$store.dispatch("actionCheckApiError", e);
        this.$store.commit("openSnackBar", "Problem z pobieraniem danych");
      }
    },
  },
  data() {
    return {
      news: [],
    };
  },
  beforeMount() {
    this.getNews();
    if (this.$store.getters["isLoggedIn"]) {
      router.push(`/${this.$store.getters["userType"]}/home`);
    }
  },
};
</script>

<style scoped>
label {
  font-size: 4vw;
}

.welcome-img {
  width: 40vw;
  height: 40vh;
  object-fit: contain;
}
</style>
