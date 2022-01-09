<template>
  <div class="max-screen-space-container flex-row-items-start">
    <div class="flex-column-items-centered">
      <ChangePassword />
    </div>
  </div>
</template>

<script>
import ChangePassword from '../../components/ChangePassword.vue'

export default {
  name: 'AdminPage',
  components: {
    ChangePassword,
  },
}
</script>

<style scoped>

</style>
