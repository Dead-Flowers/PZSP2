import Router from 'vue-router'
import Admin from '../views/admin/Admin.vue'
import AdminPage from '../views/admin/AdminPage.vue'
import AnalysisView from '../views/doctor/AnalysisView.vue'
import AnalysisStarted from '../views/doctor/AnalysisStarted.vue'
import NewAnalysis from '../views/doctor/NewAnalysis.vue' 
import NewPatient from '../views/admin/NewPatient.vue'
import AssignDoctorToPatient from '../views/admin/AssignDoctorToPatient.vue'
import NewDoctor from '../views/admin/NewDoctor.vue'
import PageNotFound from '../views/common/PageNotFound.vue'
import PatientData from '../views/doctor/PatientData.vue'
import RecordingsData from '../views/doctor/RecordingsData.vue'
import PatientPage from '../views/patient/PatientPage.vue'
import Patient from '../views/patient/Patient.vue'
import PatientAnalyses from '../views/patient/PatientAnalyses.vue'
import DoctorPage from '../views/doctor/DoctorPage'
import Doctor from '../views/doctor/Doctor'
import Welcome from '../views/common/Welcome.vue'
import LoginView from '../views/common/LoginView.vue'
import SearchForPatient from '../views/doctor/SearchForPatient.vue'
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
      beforeEnter: async (to, from, next) => {
        if(store.getters["isLoggedIn"] == null)
          await store.dispatch("actionCheckLoggedIn")
        if(!store.getters["isLoggedIn"] || store.getters["userType"] != "admin"){
          next({ name: "WelcomePage"  })
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
      beforeEnter: async (to, from, next) => {
        if(store.getters["isLoggedIn"] == null)
          await store.dispatch("actionCheckLoggedIn")
        if(!store.getters["isLoggedIn"] || store.getters["userType"] != "doctor"){
          next({ name: "WelcomePage"  })
        } else next()
      },
      children: [ 
        {
          path: 'analysis/:id',
          name: 'doctor_AnalysisView',
          component: AnalysisView
        },
        {
          path: 'analysisStarted/:id',
          name: 'doctor_AnalysisStarter',
          component: AnalysisStarted
        },
        {
          path: 'new-analysis/:id',
          name: 'doctor_NewAnalysis',
          component: NewAnalysis
        },
        {
          path: 'patient-data/:id',
          name: 'doctor_PatientData',
          component: PatientData
        },
        {
          path: 'home',
          name: 'doctor_Page',
          component: DoctorPage
        },
        {
          path: 'recordings/:id',
          name: 'doctor_Recordings',
          component: RecordingsData
        },
        {
          path: 'search/:target',
          name: "doctor_search",
          component: SearchForPatient
        }
      ]
    },
    {
      path: '/patient',
      name: 'patient',
      component: Patient,
      beforeEnter: async (to, from, next) => {
        if(store.getters["isLoggedIn"] == null)
          await store.dispatch("actionCheckLoggedIn")
        if(!store.getters["isLoggedIn"] || store.getters["userType"] != "patient"){
          next({ name: "WelcomePage"  })
        } else next()
      },
      children: [ 
        {
          path: 'home',
          name: 'patient_Page',
          component: PatientPage
        },
        {
          path: 'analyses',
          name: 'patient_Analyses',
          component: PatientAnalyses
        },
      ]
    },
    // patient
    
  ]
})