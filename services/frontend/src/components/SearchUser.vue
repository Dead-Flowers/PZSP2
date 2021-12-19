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
    <table v-if="foundUsers">
      <tr>
        <th> Pesel/Numer paszportu </th>
        <th> Imie </th>
        <th> Nazwisko </th>
      </tr>
      <tr 
        v-bind:key="user.id" 
        v-for="user in this.userList"
      >
        <td>
          <input 
            type="button"
            @click="(e)=>{chooseUser(user.id, user); e.target.value='x';}"
          />
          {{ ( user.pesel == null) ? user.passport_num : user.pesel }}
        </td>
        <td>{{`${user.first_name} ${user.second_name}`}}</td>
        <td>{{user.last_name}}</td>
      </tr>
    </table>
  </div>  
</template>

<script>
import { api } from '@/api';

export default {
  name: 'SearchUser',
  props: ['searchUser', 'userType'],
  data() {
    return {
      //TODO: refactor userid useridtype handling 
      userIdType: 'pesel',
      userId: null,
      id: null,
      firstName: null,
      secondName: null,
      surname: null,
      email: null,
      userList: [],
      foundUsers: false,
      chosenUserId: null,
    }
  },
  methods: {
    changeUserIdType(event) {
      this.userIdType = event.target.value;
    },
    async searchForUser() {
      //TODO: REFACTOR THIS PLS
      //TODO: unify naming and names last/sur name
      let params = {}
      if(this.firstName != null) {
        params["first_name"] = this.firstName
      }
      if(this.secondName != null) {
        params["second_name"] = this.secondName
      }
      if(this.surname != null) {
        params["last_name"] = this.surname
      }
      if(this.email != null) {
        params["email"] = this.email
      }
      if(this.userId != null) {
        if(this.userIdType == "pesel") {
          params["pesel"] = this.userId
        } else {
          params["pass_num"] = this.userId
        }
      }

      try {
        let respone ;
        if (params != {}) {
          respone = await api.getUsers(this.$store.getters["token"], params)
        } else {
          respone = await api.getUsers(this.$store.getters["token"], undefined)
        }
        console.log(respone)
        this.userList = respone.data
      } catch(error) {
        console.log(error)
      }
      console.log(this.userList)
      if (!this.foundUsers) this.foundUsers = true;
      console.log(this.chosenUserId);
      if(this.chosenUserId != null)
        this.searchUser(this.chosenUserId)
    },
    chooseUser(id) {
      this.chosenUserId = id;
    }
  },
  mounted() {
    //change this to users
    // this.userList = this.$store.getters.getPatients
  },
}
</script>

<style scoped>
.input-element-addon {
  margin-inline-start: 20px;
}
</style>
