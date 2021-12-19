<template>
  <div class="sector flex-column-items-centered">
    <label> Wyszukaj po peselu lub numerze paszportu </label> 
    <select 
      id="user-id-type-selector"
      class="input-element-standard input-element-addon keyboard-input input-element-small"
      name="user-id-type"
      @change="changeUserIdType($event)"
    >
      <option value="pesel">Pesel</option>
      <option value="passport-id">Nr paszportu</option>
    </select>
    <input
      id="user-id"
      class="input-element-standard input-element-addon keyboard-input"
      v-bind:type="[userIdType=='pesel' ? 'number': 'text']"
      v-bind:name="userIdType"
      v-bind:placeholder="[userIdType=='pesel' ? 'Pesel...': 'Nr paszportu...']"
      v-model="userId"
      autocomplete="off"
    />
    <label style="margin-block-start: 30px"> Wyszukaj po imieniu i nazwisku </label> 
    <input
      class="input-element-standard input-element-addon keyboard-input"
      type="text"
      name="first-name"
      placeholder="Pierwsze Imię..."
      v-model="firstName"
      autocomplete="off"
    />
    <input
      class="input-element-standard input-element-addon keyboard-input"
      type="text"
      name="second-name"
      placeholder="Drugie Imię (opcjonalnie)..."
      v-model="secondName"
      autocomplete="off"
    />
    <input
      class="input-element-standard input-element-addon keyboard-input"
      type="text"
      name="surname"
      placeholder="Nazwisko..."
      v-model="surname"
      autocomplete="off"
    />   
    <input
      class="input-element-standard input-element-addon"
      type="button"
      name="button"
      value="Wyszukaj"
      @click="searchForUser"
    />
  </div>  
</template>

<script>

export default {
  name: 'SearchUser',
  props: ['searchUser', 'userType'],
  data() {
    return {
      userIdType: 'pesel',
      userId: null,
      firstName: null,
      secondName: null,
      surname: null,
      userList: [],
    }
  },
  methods: {
    changeUserIdType(event) {
      this.userIdType = event.target.value;
    },
    searchForUser() {
      if (this.verifyUser()) {
        this.userFound();
      }
      else {
        this.userNotFound();
      }
    },
    verifyUser () {
      // this is a mock
      return this.userId=='11111' || `${this.firstName} ${this.secondName} ${this.surname}`=="Bonifacy Rupert Gąska";
    },
    userFound() {
      this.searchUser();
    },
    userNotFound() {
      alert('Nie znaleziono użytkownika');
    },
  },
  mounted() {
    //change this to users
    this.userList = this.$store.getters.getPatients
  }
}
</script>

<style scoped>
.input-element-addon {
  margin-inline-start: 20px;
}
</style>
