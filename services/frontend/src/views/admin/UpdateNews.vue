<template>
  <div>
    <UpdateNews v-bind:newsId="this.$route.params.id" />
  </div>
</template>

<script>
import UpdateNews from "../../components/UpdateNews.vue";

export default {
  name: "UpdatingNews",
  components: {
    UpdateNews,
  },
};
</script>

<style>
</style>
