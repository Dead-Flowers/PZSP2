import Router from 'vue-router'
import AdminPage from '../views/admin/AdminPage.vue'
import AnalysisView from '../views/doctor/AnalysisView.vue'
import FirstLogin from '../views/doctor/FirstLogin.vue'
import NewAnalysis from '../views/doctor/NewAnalysis.vue' 
import NewPatient from '../views/admin/NewPatient.vue'
import AssignDoctorToPatient from '../views/admin/AssignDoctorToPatient.vue'
import NewDoctor from '../views/admin/NewDoctor.vue'
import PageNotFound from '../views/common/PageNotFound.vue'
import PatientData from '../views/doctor/PatientData.vue'
import PatientPage from '../views/patient/PatientPage.vue'
import DoctorPage from '../views/doctor/DoctorPage'
import Welcome from '../views/common/Welcome.vue'
import LoginView from '../views/common/LoginView.vue'


export default new Router({
  mode: 'history',
  routes : [
    {
      path: '/',
      name: 'WelcomePage',
      component: Welcome
    },
    {
      path: "*", 
      name: 'PageNotFound',
      component: PageNotFound 
    },
    {
      path: '/login',
      name: 'LoginPage',
      component: LoginView
    },
    // admin
    {
      path: '/admin/home',
      name: 'admin_Page',
      component: AdminPage
    },
    {
      path: '/admin/register-patient',
      name: 'admin_NewPatient',
      component: NewPatient
    },
    {
      path: '/admin/register-doctor',
      name: 'admin_NewDoctor',
      component: NewDoctor
    },
    {
      path: '/admin/register-completed',
      name: 'register-completed',
      component: NewDoctor
    },
    {
      path: '/admin/assign-d2p',
      name: 'admin_assignD2P',
      component: AssignDoctorToPatient
    },
    // doctor
    {
      path: '/doctor/analysis-view',
      name: 'doctor_AnalysisView',
      component: AnalysisView
    },
    {
      path: '/doctor/new-analysis',
      name: 'doctor_NewAnalysis',
      component: NewAnalysis
    },
    {
      path: '/doctor/patient-data',
      name: 'doctor_PatientData',
      component: PatientData
    },
    {
      path: '/doctor/home',
      name: 'doctor_Page',
      component: DoctorPage
    },
    {
      path: '/doctor/newuserfirstsetupofpasswd',
      name: 'doctor_SetPassword',
      component: FirstLogin
    },
    // patient
    {
      path: '/patient/home',
      name: 'patient_Page',
      component: PatientPage
    },
  ]
})