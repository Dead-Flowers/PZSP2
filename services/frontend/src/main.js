import Vue from 'vue'
import VueRouter from 'vue-router';
import router from './router'
import App from './App.vue'
import store from './store'

Vue.config.productionTip = false
Vue.use(VueRouter);

axios.defaults.baseURL = 'http://'+ window.location.hostname +':5000/';  // the FastAPI backend

new Vue({
  render: h => h(App),
  store,
  router: router
}).$mount('#app')
