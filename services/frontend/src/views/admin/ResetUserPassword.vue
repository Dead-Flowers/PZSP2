<template>
	<div>
		<v-card>
			<v-card-title>Dane Użytkownika </v-card-title>
			<v-card-text>
				<div>Rola: {{ this.getUserRole(this.userInfo["role"]) }}</div>
				<div v-if="this.userInfo['pesel'] != null">Pesel: {{ this.userInfo["pesel"] }}</div>
				<div>Imie: {{ this.userInfo["first_name"] }}</div>
				<div v-if="this.userInfo['second_name'] != null">Drugie imie: {{ this.userInfo['second_name'] }}</div>
				<div>Nazwisko: {{ this.userInfo['last_name'] }} </div>
			</v-card-text> 
		</v-card>

		<div v-if="passwordReset">
      <h1> Rejestracja zakończona  </h1> 
      <h3>  Zapisz nowe hasło: {{ this.password }} </h3>
      <v-divider/>
    </div>
		<v-btn
			color="success"
			class="mr-4"
			@click="resetPassword()"
			style="marginBlockStart: 20px"
		>
      Zresetuj Hasło
    </v-btn>
	</div>	
</template>

<script>
import { generatePassword } from "@/utils.js"
import { api } from "@/api";

export default {
  name: "ResetUserPassword",
	data() {
		return {
			userInfo: null,
			passwordReset: false,
			password: null,
		}
	},
  methods: {
		resetPassword() {
			this.password = generatePassword()
			this.passwordReset = true
			console.log(this.password) // backend connection
		},
		getUserRole(role) {
			return role == 'admin' ? "Admin" 
			: role == 'doctor' ? "Doktor"
			: role == 'patient' ? "Pacjent"
			: null;
		},
    async getUserData(id) {
      // fetch user data
      try {
        const responeUser = await api.getUser(this.$store.getters["token"], id);
        this.userInfo = responeUser.data;
      } catch (e) {
        this.$store.dispatch("actionCheckApiError", e);
        this.$store.commit("openSnackbar", "Problem z pobieraniem danych pacjneta ");
      }
    },
  },
  beforeMount() {
    this.getUserData(this.$route.params.id);
  },
};
</script>

<style>

</style>
