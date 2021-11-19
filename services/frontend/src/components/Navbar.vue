<template>
  <div class="navbar">
    <div class="navbar-start">
      <router-link class="page-name link" to="/home">Bowel Lab</router-link>
      <div class="tab-space">
        <router-link to="/home">
          <input 
            class="tab"
            type="button"
            value="Profil"
          />
        </router-link>
        <router-link to="/new-analysis">
          <input 
          class="tab"
          type="button"
          value="Nowa Analiza"
          />
        </router-link>
        <router-link to="/patient-data">
          <input 
          class="tab"
          type="button"
          value="Pacjenci"
          />
        </router-link>
        <!-- future tabs
        template 
        <router-link to="    ">
          <input 
          class="tab"
          type="button"
          value="      "
          />
        </router-link>
        -->
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
  methods: {
    logout: function (event) {
      console.log("Logged out", event);
      router.push('/');
      
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
}

.tab:hover {
  filter: brightness(90%);
}
</style>