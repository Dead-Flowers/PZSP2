<template>
  <div class="sector flex-column-items-start">
    <label> Kryteria wyszukiwania (nie wszystkie są wymagane)</label>
    <div class="flex-row-items-start" >
      <select 
        id="user-id-type-selector"
        class="input-element-standard input-element-addon keyboard-input"
        name="user-id-type"
        @change="changeUserIdType($event)"
      >
        <option value="pesel">Pesel</option>
        <option value="passport-id">Nr paszportu</option>
      </select>
      <input
        id="user-id"
        class="input-element-standard input-element-addon keyboard-input"
        type="text"
        v-bind:name="userIdType"
        v-bind:placeholder="[userIdType=='pesel' ? 'Pesel...': 'Nr paszportu...']"
        v-model="userId"
        autocomplete="off"
      />
    </div>
    <div class="flex-row-items-start" >
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
        placeholder="Drugie Imię..."
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
    </div> 
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
            @click="searchUser(user)"
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
        params["first_name"] = this.firstName;
      }
      if(this.secondName != null) {
        params["second_name"] = this.secondName;
      }
      if(this.surname != null) {
        params["last_name"] = this.surname;
      }
      if(this.email != null) {
        params["email"] = this.email;
      }
      if(this.userId != null) {
        if(this.userIdType == "pesel") {
          params["pesel"] = this.userId;
        } else {
          params["pass_num"] = this.userId;
        }
      }
      try {
        let respone ;
        if (params != {}) {
          respone = await api.getUsers(this.$store.getters["token"], params);
        } else {
          respone = await api.getUsers(this.$store.getters["token"], undefined);
        }
        console.log(respone)
        let unfilteredUserList = respone.data
        unfilteredUserList.forEach(element => {
          if (element.role == this.userType) this.userList.push(element);
        });

      } catch(error) {
        console.log(error)
      }
      console.log(this.userList)
      if (this.userList.length > 0) this.foundUsers = true;
    },
  },
  mounted() {
    //change this to users
    // this.userList = this.$store.getters.getPatients
  },
}
</script>

<style scoped>
.input-element-addon {
  margin-inline-start: 2vw;
}
label {
  font-size: 1.5vw;
}
</style>