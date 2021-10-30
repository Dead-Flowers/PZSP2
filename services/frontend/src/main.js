import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios';

Vue.config.productionTip = false

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000/';  // the FastAPI backend

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
