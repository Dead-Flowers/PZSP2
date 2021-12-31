import Vue from 'vue';
import VueRouter from 'vue-router';
import Vuetify from '@/plugins/vuetify';
import router from './router';
import App from './App.vue';
import store from './store';
import axios from 'axios';
import ECharts from 'vue-echarts';
import { use } from 'echarts/core';
import 'vuetify/dist/vuetify.min.css';
import {
  CanvasRenderer
} from 'echarts/renderers';
import {
  BarChart
} from 'echarts/charts';
import {
  GridComponent,
  TooltipComponent
} from 'echarts/components';


Vue.config.productionTip = false
Vue.use(VueRouter);

use([
  CanvasRenderer,
  BarChart,
  GridComponent,
  TooltipComponent
]);

axios.defaults.baseURL = 'http://'+ window.location.hostname +':5000/';  // the FastAPI backend

Vue.component('v-chart', ECharts)

new Vue({
  render: h => h(App),
  store,
  router: router,
  vuetify: Vuetify
}).$mount('#app')
