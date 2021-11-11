<template>
  <div class="navbar">
    <div class="navbar-start">
      <label class="page-name">Bowel Lab</label>
      <div class="tab-space">
        <input 
        class="tab-bookmark tab"
        type="button"
        value="Nowa Analiza"
        />
        <input 
        class="tab-bookmark tab"
        type="button"
        value="Pacjenci"
        />
        <input 
        class="tab-bookmark tab"
        type="button"
        value="Wyniki"
        />
        <!-- future tabs-->
      </div>
    </div>
    
    <div class="navbar-end">
      <input 
        class="tab"
        type="button"
        value="Wyloguj"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'Navbar'
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

.tab-bookmark {
  opacity: 0.8;
  margin-block-start: 3px;
  padding-block: 15px;
  width: var(--width-navbar);
}

.tab {
  background-color: var(--color-tab-bookmark);
  border: 0;
  padding: 20px;
  font-size: 1rem;
  font-family:  "Roboto", sans-serif;
  color: var(--color-text);
}

.tab:hover {
  filter: brightness(90%);
}
</style>