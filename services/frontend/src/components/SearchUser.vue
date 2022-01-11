<template>
  <div>
    <h3>Kryteria wyszukiwania (nie wszystkie są wymagane)</h3>
    <v-form
      ref="form"
      @submit="
        (e) => {
          e.preventDefault();
          searchForUser();
        }
      "
    >
      <v-select
        v-model="userIdType"
        :items="userIdTypeList"
        label="Rodzaj numeru identyfikacyjnego"
      />
      <v-text-field
        id="user-id"
        v-model="userId"
        v-bind:label="userIdType == 'pesel' ? 'Pesel...' : 'Nr paszportu...'"
      />
      <v-text-field v-model="first_name" label="Pierwsze Imię" />
      <v-text-field v-model="second_name" label="Drugie Imię" />
      <v-text-field v-model="last_name" label="Nazwisko" />
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
      :items="user_list"
      :single-select="true"
      item-key="id"
      :show-select="true"
      :multi-sort="true"
      checkbox-color="red"
    >
      <template slot="item.data-table-select" slot-scope="{ item }">
        <v-btn @click="selectUser(item)">
          <v-icon>mdi-play</v-icon>
          Wybierz
        </v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import { api } from "@/api";
export default {
  name: "SearchUser",
  props: ["searchUser", "userType"],
  data() {
    return {
      userIdType: "pesel",
      userIdTypeList: ["pesel", "nr paszportu"],
      userId: null,
      first_name: null,
      second_name: null,
      last_name: null,
      user_list: [],
      foundUsers: false,
      selected_user: [],
      headers: [
        { text: "Pesel", align: "start", value: "pesel" },
        { text: "Pierwsze Imię", value: "first_name" },
        { text: "Drugie Imię", value: "second_name" },
        { text: "Nazwisko", value: "last_name" },
        { text: "Wybór", value: "data-table-select" },
      ],
    };
  },
  methods: {
    createParams() {
      //TODO: refactor userID maybe?
      let params = {};
      if (this.first_name != null) {
        params["first_name"] = this.first_name;
      }
      if (this.second_name != null) {
        params["second_name"] = this.second_name;
      }
      if (this.last_name != null) {
        params["last_name"] = this.last_name;
      }
      if (this.email != null) {
        params["email"] = this.email;
      }
      if (this.userId != null) {
        if (this.userIdType == "pesel") {
          params["pesel"] = this.userId;
        } else {
          params["pass_num"] = this.userId;
        }
      }
      return params;
    },
    async getUsers(params) {
      let respone;
      if (params != {}) {
        respone = await api.getUsers(this.$store.getters["token"], params);
      } else {
        respone = await api.getUsers(this.$store.getters["token"], undefined);
      }
      let unfilteredUserList = respone.data;
      unfilteredUserList.forEach((element) => {
        if (element.role == this.userType) this.user_list.push(element);
      });
    },
    async searchForUser() {
      this.user_list = [];
      let params = this.createParams();

      try {
        await this.getUsers(params);
      } catch (error) {
        console.log(error);
        this.$store.dispatch("actionCheckApiError", error);
        this.$store.commit(
          "openSnackbar",
          "Wystąpił błąd podczas wyszukiwania"
        );
      }

      this.foundUsers = true;
    },
    async selectUser(user) {
      this.selected_user = null;
      this.searchUser(user);
    },
  },
  mounted() {
    this.user_list = [];
    this.foundUsers = false;
  },
};
</script>

<style scoped>
</style>