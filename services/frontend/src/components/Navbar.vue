<template>
  <v-navigation-drawer app dark expand-on-hover permanent>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="text-h6">
          <font-awesome-icon icon="flask" />
          BowelLab
        </v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    
    <v-divider />

    <!-- doctor tabs -->
    <v-list
      dense
      nav
      v-if="getUserType() == 'doctor'"
    >
      <v-list-item @click="goToPage('/doctor/home')">
        <v-list-item-icon>
          <font-awesome-icon icon="user-circle" />
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Profil
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item @click="goToPage('/doctor/search/new-analysis')">
        <v-list-item-icon>
          <font-awesome-icon icon="plus-square" />
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Nowa Analiza
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item @click="goToPage('/doctor/search/patient-data')">
        <v-list-item-icon>
          <font-awesome-icon icon="list" />
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Dane i Analizy Pacjentów
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item @click="goToPage('/doctor/search/recordings')">
        <v-list-item-icon>
          <font-awesome-icon icon="file-audio" />
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Nagrania
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

    </v-list>

    <!-- admin tabs -->
    <v-list
      dense
      nav
      v-if="getUserType() == 'admin'"
    >
      <v-list-item @click="goToPage('/admin/home')">
        <v-list-item-icon>
          <font-awesome-icon icon="user-circle" />
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Profil
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item @click="goToPage('/admin/new-admin')">
        <v-list-item-icon>
          <font-awesome-icon icon="user-shield" />
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Zarejestruj Admina
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item @click="goToPage('/admin/register-patient')">
        <v-list-item-icon>
          <font-awesome-icon icon="user-plus" />
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Zarejestruj Pacjenta
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item @click="goToPage('/admin/register-doctor')">
        <v-list-item-icon>
          <font-awesome-icon icon="user-nurse" />
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Zarejestruj Doktora
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item @click="goToPage('/admin/assign-d2p')">
        <v-list-item-icon>
          <font-awesome-icon icon="people-arrows" />
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Przypisz pacjenta
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item @click="goToPage('/admin/search/reset-password')">
        <v-list-item-icon>
          <font-awesome-icon icon="unlock-alt" />
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Zresetuj hasło
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

    </v-list>

    <!-- patient tabs -->
    <v-list
      dense
      nav
      v-if="getUserType() == 'patient'"
    >
      <v-list-item @click="goToPage('/patient/home')">
        <v-list-item-icon>
          <font-awesome-icon icon="user-circle" />
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Profil
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item @click="goToPage('/patient/analyses')">
        <v-list-item-icon>
          <font-awesome-icon icon="list" />
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Moje analizy
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    
    </v-list>
    <v-footer 
      absolute
    >
      <div style="display: flex" >
        <font-awesome-icon 
          icon="sign-out-alt" 
          style="font-size: 3vh; margin-inline-end: 25px"
          @click="logout"/>
        <v-btn
          color="primary"
          elevation="2"
          large
          outlined
          @click="logout"
        >
          Wyloguj
        </v-btn>
      </div>
    </v-footer>
  </v-navigation-drawer>
</template>

<script>
import router from '../router'

export default {
  name: 'Navbar',
  methods: {
    logout: function (event) {
      this.$store.dispatch("actionLogOut")
      console.log("Logged out", event);
      router.push(`/`);
    },
    getUserType() {
      return this.$store.getters["userType"];
    },
    goToPage(link){
      router.push(link);
    }

  }
}
</script>

<style scoped>
</style>