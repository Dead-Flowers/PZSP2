<template>
  <div>
    <h3> Kryteria wyszukiwania (nie wszystkie są wymagane)</h3>
    <v-form
      ref="form"
      @submit="(e) => {e.preventDefault(); searchForUser();}"
    >
      <v-select
        v-model="userIdType"
        :items="userIdTypeList"
        label="Rodzaj numeru identyfikacyjnego"
      />
      <v-text-field
        id="user-id"
        v-model="userId"
        v-bind:label="userIdType=='pesel' ? 'Pesel...': 'Nr paszportu...'"
      />
      <v-text-field
        v-model="firstName"
        label="Pierwsze Imię"
      />
      <v-text-field
        v-model="secondName"
        label="Drugie Imię"
      />
      <v-text-field
        v-model="last_name"
        label="Nazwisko"
      />
      <v-btn
        color="success"
        class="mr-4"
        type="submit"
        style="margin-block-end: 10px"
      >
        Wyszukaj
      </v-btn>
    </v-form>
    
    <v-data-table
      v-if="foundUsers"
      v-model="selected_user"
      :headers="headers"
      :items="userList"
      :single-select="true"
      item-key="userID"
      show-select
      class="elevation-1"
    >
    <template v-slot:top>
      <v-btn
        :disabled="!selected_user"
        color="success"
        class="mr-4"
        @click="initSearch"
      >
      Wybierz zaznaczonego użytkownika
      </v-btn>
    </template>
    </v-data-table>
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
      userIdTypeList: ['pesel', 'nr paszportu'],
      userId: null,
      firstName: null,
      secondName: null,
      last_name: null,
      userList: [],
      foundUsers: false,
      selected_user: [],
      headers: [
        { text:"Pesel", value: "pesel"},
        { text:"Pierwsze Imię", value: "first_name"},
        { text:"Drugie Imię", value: "second_name"},
        { text:"Nazwisko", align: "start", value: "last_name"},
      ],
    }
  },
  methods: {
    async searchForUser() {
      this.userList = [];
      //TODO: REFACTOR THIS PLS
      //TODO: unify naming and names last/sur name
      let params = {}
      if(this.firstName != null) {
        params["first_name"] = this.firstName;
      }
      if(this.secondName != null) {
        params["second_name"] = this.secondName;
      }
      if(this.last_name != null) {
        params["last_name"] = this.last_name;
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
    initSearch() {
      this.userList = [];
      this.foundUsers = false;
      this.searchUser(this.selected_user[0]);
      this.selected_user = null;
    },
  },
  mounted() {
      this.userList = [];
      this.foundUsers = false;
  },
}
</script>

<style scoped>

</style>