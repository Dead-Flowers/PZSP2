<template>
  <div style="display:flex">
    <div style="width: 40vw">
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
      <v-expansion-panels accordion>
        <v-expansion-panel
          v-for="n in news"
          :key="n.id"
        >
          <v-expansion-panel-header>{{n.title}} </v-expansion-panel-header>
          <v-expansion-panel-content>
            {{n.description}}
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </div>
    <img src="doctor.png" class="welcome-img"/>
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
      news: [
        {
          id: 1,
          title: 'Panel Pacjenta',
          description: 'Stworzono nowy Panel Pacjenta. W tym panelu pacjent ma możliwość przegldania wasnych analiz.',
        },
        {
          id: 2,
          title: 'Zmiana biblioteki stylów',
          description: 'Seriws został odświeżony przy użyciu Vuetify.',
        },
        {
          id: 3,
          title: 'Wesołych Świąt',
          description: 'Zespół BowelLab chciałby życzyć wszystkim użytkownikom wesołych świąt i szczęśliwego nowego roku.',
        },
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
