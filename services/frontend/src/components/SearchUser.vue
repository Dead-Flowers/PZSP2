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
    <tabel v-if="foundUsers">
      <tr>
        <th> Id </th>
        <th> Imie </th>
        <th> Nazwisko </th>
      </tr>
      <tr 
        v-bind:key="user.userId" 
        v-for="user in userList"
      >
        <td>
          <inptu 
            type="checkbox"
            v-model="chosenUser"
            v-on="chosenUser = $event.target.value"
            :value="user.userId"
          />
          {{`${user.userIdType} - ${user.userId}` }}
        </td>
        <td>{{`${user.userFirstName} ${user.userSecondName}`}}</td>
        <td>{{user.userSurname}}</td>
      </tr>
    </tabel>
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
      userList: [
        {
          userIdType: 'pesel',
          userId: 1111,
          userFirstName: aaa,
          userSecondName: bbb,
          userSurname: ccc,
        },
        {
          userIdType: 'pesel',
          userId: 12,
          userFirstName: ddd,
          userSecondName: fff,
          userSurname: eee,
        },
      ],
      foundUsers: false,
      chosenUser: null,
    }
  },
  methods: {
    changeUserIdType(event) {
      this.userIdType = event.target.value;
    },
    searchForUser() {
      if (!this.foundUsers) this.foundUsers = true;
      else {
        console.log(this.chosenUser);
      }
    },
    verifyUser () {
      // this is a mock
      return this.userId=='11111' || `${this.firstName} ${this.secondName} ${this.surname}`=="Bonifacy Rupert Gąska";
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
