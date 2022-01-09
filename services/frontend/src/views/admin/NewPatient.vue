<template>
  <div class="max-screen-space-container flex-row-items-start">
    <div class="navbar-as-adjacent flex-column-items-centered">
      <RegisterUserForm v-bind:usertype="'patient'"/>
    </div>
  </div>
</template>

<script>
import RegisterUserForm from '../../components/RegisterUserForm.vue'

export default {
  name: 'NewPatient',
  components: {
    RegisterUserForm,
  },
}
</script>

<style>

</style>
