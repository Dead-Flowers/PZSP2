<template>
  <div class="max-screen-space-container flex-row-items-start">
    <div class="navbar-as-adjacent flex-column-items-centered">
      <RegisterUserForm v-bind:usertype="'doctor'" />
    </div>
  </div>
</template>

<script>
import RegisterUserForm from '../../components/RegisterUserForm.vue'

export default {
  name: 'NewDoctor',
  components: {
    RegisterUserForm,
  },
}
</script>

<style>

</style>
