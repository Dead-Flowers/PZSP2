<template>
  <div>
    <RegisterUserForm v-bind:usertype="'patient'"/>
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
