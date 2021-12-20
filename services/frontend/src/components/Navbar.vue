<template>
  <div class="navbar">
    <div class="navbar-start">
      <div class="page-name-container">
        <router-link class="page-name link" to='/' >Bowel Lab</router-link>
      </div>
      <!-- doctor tabs -->
      <div v-if="(usertype == 'doctor')" class="tab-space">
        <router-link to='/doctor/home'>
          <input 
            class="tab"
            type="button"
            value="Profil"
          />
        </router-link>
        <router-link to='/doctor/new-analysis' >
          <input 
            class="tab"
            type="button"
            value="Nowa Analiza"
          />
        </router-link>
        <router-link to='/doctor/patient-data'>          
          <input 
            class="tab"
            type="button"
            value="Pacjenci"
          />
        </router-link>
      </div>
      <!-- admin tabs -->
      <div v-if="(usertype == 'admin')" class="tab-space">
        <router-link to='/admin/home'>
          <input 
            class="tab"
            type="button"
            value="Profil"
          />
        </router-link>
        <router-link to='/admin/register-patient' >
          <input 
            class="tab"
            type="button"
            value="Zarejestruj Pacjenta"
          />
        </router-link>
        <router-link to='/admin/register-doctor' >
          <input 
            class="tab"
            type="button"
            value="Zarejestruj Doktora"
          />
        </router-link>
        <router-link to='/admin/assign-d2p' >
          <input 
            class="tab"
            type="button"
            value="Przypisz doktora do pacjenta"
          />
        </router-link>
      </div>
      <!-- patient tabs -->
      <div v-if="(usertype == 'patient')" class="tab-space">
        <router-link to='/patient/home'>
          <input 
            class="tab"
            type="button"
            value="Profil"
          />
        </router-link>
      </div>
    </div>
    
    
    <div class="navbar-end flex-column-items-centered">
      <input 
        class="tab"
        type="button"
        value="Wyloguj"
        @click="logout"
      />
    </div>
  </div>
</template>

<script>
import router from '../router'

export default {
  name: 'Navbar',
  props: ['usertype'],
  methods: {
    logout: function (event) {
      this.$store.dispatch("actionLogOut")
      console.log("Logged out", event);
      router.push(`/`);
    },
  }
}
</script>

<style scoped>
.navbar {
  top: 0;
  left: 0;
  position: inherit;
  background-color: var(--color-navbar);
  margin-right: 1px;
  padding-block-start: 2vw;
  height: 100vh;
  width: var(--width-navbar);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  overflow-wrap: break-word;
}

.navbar-end {
  margin-block-end: 3vw;
}

.page-name-container {
  min-width: var(--width-navbar);
  text-align: center;
  align-items: center;
}

.page-name {
  font-size: 2vw;
  color: var(--text-color)
}

.tab-space {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.tab {
  background-color: var(--color-accent);
  border: 0;
  margin-block-start: 0.15vw;
  padding-block: 0.75vw;
  width: var(--width-navbar);
  font-size: 1.7vw;
  font-family:  "Roboto", sans-serif;
  color: var(--color-text);
  white-space: normal;
}

.tab:hover {
  filter: brightness(90%);
}
</style>