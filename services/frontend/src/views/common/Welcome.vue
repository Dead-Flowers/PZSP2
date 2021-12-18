<template>
  <div class="max-screen-space-container flex-column-items-centered">
    <div class="sector  flex-row-items-centered">
      <div class="flex-column-items-centered">
        <label>Witaj w BowelLab</label>
        <img src="doctor.png" class="welcome-img"/>
      </div>
      <div class="flex-column-items-start">
        <label> Aktualności </label>  
        <ul>
        <li> <a href="https://www.w3schools.com"> Nowa aktualizacja 03.12.2021 </a>   </li>
        <li> <a href="https://www.w3schools.com"> Od teraz kontakt z administratorem jeszcze łatwiejszy </a> </li>
        <li> <a href="https://www.w3schools.com"> Zapraszamy wszystkich do wypełniania ankiety </a> </li>
        <li> <a href="https://www.w3schools.com"> Została wprowadzona nowa szata graficzna </a> </li>
        </ul>
        <router-link to='/doctor/Login' class="input-element-standard"> Panel Lekarza </router-link>
        <router-link to='/patient/Login' class="input-element-standard"> Panel Pacjenta </router-link>
        <router-link to='/admin/Login' class="input-element-standard"> Panel Admina </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Welcome',
  components: {
  }
}
</script>

<style scoped>
label {
  font-size: 4rem;
}

.welcome-img {
  width: 60%;
  height: 60%;
  object-fit: contain;

}
</style>
