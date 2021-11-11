import Router from 'vue-router'
import Admin from '../views/Admin.vue'
import AnalysisData from '../views/AnalysisData.vue'
import FirstLogin from '../views/FirstLogin.vue'
import Login from '../views/Login.vue'
import NewAnalysis from '../views/NewAnalysis.vue' 
import PageNotFound from '../views/PageNotFound.vue'
import PatientData from '../views/PatientData.vue'
import Profile from '../views/Profile.vue'
import NewPatient from '../views/NewPatient.vue'


export default new Router({
  mode: 'history',
  routes : [
    {
      path: '/admin',
      name: 'Admin',
      component: Admin
    },
    {
      path: '/',
      name: 'Analysis Data',
      component: AnalysisData
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
      path: '/profile',
      name: 'Profile',
      component: Profile
    },
    {
      path: '/register-patient',
      name: 'nEWPatient',
      component: NewPatient
    },
    {
      path: '/newuserfirstsetupofpasswd',
      name: 'Ustaw Hasło',
      component: FirstLogin
    },
    {
      path: "*", 
      name: 'PageNotFound',
      component: PageNotFound }
  ]
})