import Router from 'vue-router'
import Admin from '../views/admin/Admin.vue'
import AdminPage from '../views/admin/AdminPage.vue'
import AnalysisView from '../views/doctor/AnalysisView.vue'
import NewAnalysis from '../views/doctor/NewAnalysis.vue' 
import NewPatient from '../views/admin/NewPatient.vue'
import AssignDoctorToPatient from '../views/admin/AssignDoctorToPatient.vue'
import NewDoctor from '../views/admin/NewDoctor.vue'
import PageNotFound from '../views/common/PageNotFound.vue'
import PatientData from '../views/doctor/PatientData.vue'
import PatientPage from '../views/patient/PatientPage.vue'
import Patient from '../views/patient/Patient.vue'
import DoctorPage from '../views/doctor/DoctorPage'
import Doctor from '../views/doctor/Doctor'
import Welcome from '../views/common/Welcome.vue'
import LoginView from '../views/common/LoginView.vue'
import store from '@/store'

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
      path: '/admin',
      name: 'admin',
      component: Admin,
      beforeEnter: (to, from, next) => {
        if(!store.getters["isLoggedIn"] || store.getters["userType"] != "admin"){
          next({ name: "Welcome"  })
        } else next()
      },
      children: [
        {
          path: 'home',
          name: 'admin_Page',
          component: AdminPage
        },
        {
          path: 'register-patient',
          name: 'admin_NewPatient',
          component: NewPatient
        },
        {
          path: 'register-doctor',
          name: 'admin_NewDoctor',
          component: NewDoctor
        },
        {
          path: 'register-completed',
          name: 'register-completed',
          component: NewDoctor
        },
        {
          path: 'assign-d2p',
          name: 'admin_assignD2P',
          component: AssignDoctorToPatient
        },
      ]
    },
    {
      path: '/doctor',
      name: 'doctor',
      component: Doctor,
      beforeEnter: (to, from, next) => {
        if(!store.getters["isLoggedIn"] || store.getters["userType"] != "doctor"){
          next({ name: "Welcome"  })
        } else next()
      },
      children: [ 
        {
          path: 'analysis-view',
          name: 'doctor_AnalysisView',
          component: AnalysisView
        },
        {
          path: 'new-analysis',
          name: 'doctor_NewAnalysis',
          component: NewAnalysis
        },
        {
          path: 'patient-data',
          name: 'doctor_PatientData',
          component: PatientData
        },
        {
          path: 'home',
          name: 'doctor_Page',
          component: DoctorPage
        },
      ]
    },
    {
      path: '/patient',
      name: 'patient',
      component: Patient,
      beforeEnter: (to, from, next) => {
        if(!store.getters["isLoggedIn"] || store.getters["userType"] != "patient"){
          next({ name: "Welcome"  })
        } else next()
      },
      children: [ 
        {
          path: '/home',
          name: 'patient_Page',
          component: PatientPage
        },
      ]
    },
    // patient
    
  ]
})