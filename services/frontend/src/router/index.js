import Router from 'vue-router'
import Admin from '../views/admin/Admin.vue'
import AdminPage from '../views/admin/AdminPage.vue'
import AnalysisView from '../views/common/AnalysisView.vue'
import AnalysisStarted from '../views/doctor/AnalysisStarted.vue'
import NewAnalysis from '../views/doctor/NewAnalysis.vue'
import NewPatient from '../views/admin/NewPatient.vue'
import Stats from '../views/admin/Statistics.vue'
import AssignDoctorToPatient from '../views/admin/AssignDoctorToPatient.vue'
import NewDoctor from '../views/admin/NewDoctor.vue'
import News from '../views/admin/News.vue'
import NewNews from '../views/admin/NewNews.vue'
import UpdateNews from '../views/admin/UpdateNews.vue'
import PageNotFound from '../views/common/PageNotFound.vue'
import PatientAnalyses from '../views/doctor/PatientAnalyses.vue'
import RecordingsData from '../views/doctor/RecordingsData.vue'
import PatientPage from '../views/patient/PatientPage.vue'
import Patient from '../views/patient/Patient.vue'
import UserOwnData from '../views/patient/UserOwnData.vue'
import DoctorPage from '../views/doctor/DoctorPage'
import Doctor from '../views/doctor/Doctor'
import Welcome from '../views/common/Welcome.vue'
import Goodbye from '../views/common/Goodbye.vue'
import LoginView from '../views/common/LoginView.vue'
import SearchForPatient from '../views/doctor/SearchForPatient.vue'
import SearchForUser from '../views/admin/SearchForUser.vue'
import NewAdmin from '../views/admin/NewAdmin.vue'
import ResetUserPassword from '../views/admin/ResetUserPassword.vue'
import store from '@/store'

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'WelcomePage',
      component: Welcome
    },
    {
      path: '/goodbye',
      name: 'GoodbyePage',
      component: Goodbye
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
        if (store.getters["isLoggedIn"] == null)
          await store.dispatch("actionCheckLoggedIn")
        if (!store.getters["isLoggedIn"] || store.getters["userType"] != "admin") {
          next({ name: "WelcomePage" })
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
        {
          path: 'news',
          name: 'admin_news',
          component: News,
        },
        {
          path: 'news/new',
          name: 'admin_news_new',
          component: NewNews
        },
        {
          path: 'news/edit/:id',
          name: 'admin_news_edit',
          component: UpdateNews
        },
        {
          path: 'search/:target',
          name: "admin_search",
          component: SearchForUser
        },
        {
          path: 'reset-password/:id',
          name: "admin_resetPassword",
          component: ResetUserPassword,
        },
        {
          path: 'new-admin',
          name: "admin_newAdmin",
          component: NewAdmin
        },
        {
          path: 'stats',
          name: "admin_stats",
          component: Stats
        }
      ]
    },
    {
      path: '/doctor',
      name: 'doctor',
      component: Doctor,
      beforeEnter: async (to, from, next) => {
        if (store.getters["isLoggedIn"] == null)
          await store.dispatch("actionCheckLoggedIn")
        if (!store.getters["isLoggedIn"] || store.getters["userType"] != "doctor") {
          next({ name: "WelcomePage" })
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
          component: PatientAnalyses
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
        if (store.getters["isLoggedIn"] == null)
          await store.dispatch("actionCheckLoggedIn")
        if (!store.getters["isLoggedIn"] || store.getters["userType"] != "patient") {
          next({ name: "WelcomePage" })
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
          component: UserOwnData
        },
        {
          path: 'analysis/:id',
          name: 'patient_AnalysisView',
          component: AnalysisView
        },
      ]
    },
    // patient

  ]
})