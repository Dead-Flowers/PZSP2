<template>
  <div>
    <h1>Aktualności</h1>
    <v-divider />
    <NewsData v-bind:newsId="this.$route.params.id" />
  </div>
</template>

<script>
import NewsData from "../../components/NewsData.vue";

export default {
  name: "News",
  components: {
    NewsData,
  },
};
</script>

<style>
</style>