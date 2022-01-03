<template>
  <v-navigation-drawer app dark expand-on-hover permanent>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="text-h6">
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
          <v-icon></v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Profil
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item @click="goToPage('/doctor/new-analysis')">
        <v-list-item-icon>
          <v-icon></v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Nowa Analiza
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item @click="goToPage('/doctor/patient-data')">
        <v-list-item-icon>
          <v-icon></v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Dane Pacjentów
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
          <v-icon ></v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Profil
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item @click="goToPage('/admin/register-patient')">
        <v-list-item-icon>
          <v-icon></v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Zarejestruj Pacjenta
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item @click="goToPage('/admin/register-doctor')">
        <v-list-item-icon>
          <v-icon></v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Zarejestruj Doktora
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item @click="goToPage('/admin/assign-d2p')">
        <v-list-item-icon>
          <v-icon></v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Przypisz doktora do pacjenta
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
          <v-icon></v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            Profil
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      
    </v-list>
    <v-footer absolute>
      <v-btn
        color="primary"
        elevation="2"
        large
        outlined
        @click="logout"
      >
        Wyloguj
      </v-btn>
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