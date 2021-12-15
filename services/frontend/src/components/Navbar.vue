<template>
  <div class="navbar">
    <div class="navbar-start">
      <router-link class="page-name link" to='/' >Bowel Lab</router-link>
      <!-- zakładki lekarza -->
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
      <!-- zakładki admina -->
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
      </div>
      <!-- zakładki pacjenta -->
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
      console.log("Logged out", event);
      router.push(`/${this.usertype}/login`);
      
    },
  }
}
</script>

<style scoped>
.navbar {
  top: 0;
  left: 0;
  position: fixed;
  z-index: 10;
  background-color: var(--color-navbar);
  margin: 0;
  padding-block-start: 40px;
  height: 100vh;
  width: var(--width-navbar);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  overflow-x: hidden;
}

.navbar-end {
  margin-block-end: 60px;
}

.page-name {
  font-size: 1.5rem;
  margin-inline: 15px;
}

.tab-space {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.tab {
  background-color: var(--color-tab-bookmark);
  border: 0;
  margin-block-start: 3px;
  padding-block: 15px;
  width: var(--width-navbar);
  padding: 20px;
  font-size: 1rem;
  font-family:  "Roboto", sans-serif;
  color: var(--color-text);
  overflow-wrap: break-word;
}

.tab:hover {
  filter: brightness(90%);
}
</style>