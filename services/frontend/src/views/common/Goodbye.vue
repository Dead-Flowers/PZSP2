<template>
  <div style="display: flex">
    <div style="width: 40vw">
      <h1>Do widzenia</h1>
      <v-btn
        color="primary"
        elevation="2"
        large
        outlined
        @click="goToFrontPage()"
        style="margin-block: 10px"
      >
        Powróć do strony początkowej
      </v-btn>
      
    </div>
    <img src="https://i.imgur.com/xbrA76P.gif" class="goodbye-img" />
  </div>
</template>

<script>
import router from "../../router";

export default {
  name: "Goodbye",
  methods: {
    goToFrontPage() {
      router.push("/");
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

.goodbye-img {
  width: 40vw;
  height: 40vh;
  object-fit: contain;
}
</style>
