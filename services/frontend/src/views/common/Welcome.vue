<template>
  <div style="display: flex">
      <img src="doctor.png" class="welcome-img"/>
      <div class="flex-column-items-start">
        <label>Witaj w BowelLab</label>
        <h3> Aktualności </h3>  
        <ul>
          <li> <a href="https://www.w3schools.com"> Aktualnoś </a>   </li>
          <li> <a href="https://www.w3schools.com"> Od teraz kontakt z administratorem jeszcze łatwiejszy </a> </li>
          <li> <a href="https://www.w3schools.com"> Zapraszamy wszystkich do wypełniania ankiety </a> </li>
          <li> <a href="https://www.w3schools.com"> Została wprowadzona nowa szata graficzna </a> </li>
        </ul>
        <router-link to='/login' class="input-element-standard"> Zaloguj się </router-link>
      </div>
  </div>
</template>

<script>
export default {
  name: 'Welcome',
  data () {
    return {
      colors: [
        'indigo',
        'warning',
        'pink darken-2',
        'red lighten-1',
        'deep-purple accent-4',
      ],
      slides: [
        'First',
        'Second',
        'Third',
        'Fourth',
        'Fifth',
      ],
    }
  },
}
</script>

<style scoped>
label {
  font-size: 4vw;
}

.welcome-img {
  width: 60vw;
  height: 60vh;
  object-fit: contain;
}
</style>
