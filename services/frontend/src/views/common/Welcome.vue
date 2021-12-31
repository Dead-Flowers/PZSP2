<template>
  <div>
    <div style="display:flex">
      <div style="margin: 0 auto;">
        <h1>Witaj w BowelLab</h1>
        <v-btn
          color="primary"
          elevation="2"
          large
          outlined
          @click="goToLoginPage()"
          style="margin-block: 10px"
        >
          Zaloguj się
        </v-btn>
      </div>
      <img src="doctor.png" class="welcome-img"/>
    </div>
    <v-carousel
      cycle
      height="300"
      hide-delimiter-background
      show-arrows-on-hover
    >
      <v-carousel-item
        v-for="(slide, i) in slides"
        :key="i"
      >
        <v-sheet
          :color="colors[i]"
          height="100%"
        >
          <v-row
            class="fill-height"
            align="center"
            justify="center"
          >
            <div class="text-h2">
              {{ slide }}
            </div>
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>
  </div>
</template>

<script>
import router from "../../router"
export default {
  name: 'Welcome',
  methods: {
    goToLoginPage() {
      router.push('/login');
    }
  },
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
        'Aktualność 1',
        'Aktualność 2',
        'Aktualność 3',
        'Aktualność 4',
        'Aktualność 5',
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
  width: 40vw;
  height: 40vh;
  object-fit: contain;
}
</style>
