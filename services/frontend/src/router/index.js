import Router from 'vue-router'
import Admin from '../views/Admin.vue'
import AnalysisView from '../views/AnalysisView.vue'
import FirstLogin from '../views/FirstLogin.vue'
import Login from '../views/Login.vue'
import NewAnalysis from '../views/NewAnalysis.vue' 
import NewPatient from '../views/NewPatient.vue'
import PageNotFound from '../views/PageNotFound.vue'
import PatientData from '../views/PatientData.vue'
import Profile from '../views/Profile.vue'
import Welcome from '../views/Welcome.vue'


export default new Router({
  mode: 'history',
  routes : [
    {
      path: '/',
      name: 'Welcome',
      component: Welcome
    },
    {
      path: '/admin',
      name: 'Admin',
      component: Admin
    },
    {
      path: '/analysis-view',
      name: 'AnalysisView',
      component: AnalysisView
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/new-analysis',
      name: 'New Analysis',
      component: NewAnalysis
    },
    {
      path: '/patient-data',
      name: 'Patient Data',
      component: PatientData
    },
    {
      path: '/home',
      name: 'Profile',
      component: Profile
    },
    {
      path: '/register-patient',
      name: 'NewPatient',
      component: NewPatient
    },
    {
      path: '/newuserfirstsetupofpasswd',
      name: 'SetPassword',
      component: FirstLogin
    },
    {
      path: "*", 
      name: 'PageNotFound',
      component: PageNotFound 
    }
  ]
})