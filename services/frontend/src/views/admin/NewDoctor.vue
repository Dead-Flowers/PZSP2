<template>
  <div>
    <RegisterUserForm v-bind:usertype="'doctor'" />
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
