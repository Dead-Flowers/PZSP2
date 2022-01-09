
import { createLocalVue, mount } from '@vue/test-utils'
import App from '@/App.vue'
import Vuetify from 'vuetify'
import VueRouter from 'vue-router'
import s from '@/store'
import Welcome from '@/views/common/Welcome.vue'
import { getters } from "@/store/user";
import Vuex from 'vuex'
import Router from "@/router"

import ChangePassword from '@/components/ChangePassword.vue'
import AnalysisInit from '@/components/AnalysisInit.vue'
import AnalysisResultTable from '@/components/AnalysisResultTable.vue'
import AnalysisVisualization from '@/components/AnalysisVisualization.vue'
import LoginForm from '@/components/LoginForm.vue'
import Navbar from '@/components/Navbar.vue'
import PatientTable from '@/components/PatientTable.vue'
import RecordingsTable from '@/components/RecordingsTable.vue'
import RegisterUserForm from '@/components/RegisterUserForm.vue'
import SearchUser from '@/components/SearchUser.vue'


describe('components tests', () => {
    const localVue = createLocalVue()
    let vuetify
    let router = Router
    let state
    let store
    
    localVue.use(VueRouter)

    let actions = {
      actionCheckLoggedIn: jest.fn()
    }

    beforeEach(() => {
    state = {
      isLoggedIn: false,
      userType: "doctor"
    }

    vuetify = new Vuetify()
    store = new Vuex.Store ({
      modules: {
        user: {
          state,
          actions,
          getters: getters,
        }
      }
    })
    })

    it('change password component', () => {
      const wrapper = mount(ChangePassword, {
        localVue,
        vuetify,
        router,
        store
      })

      const textFields = wrapper.findAll(".v-text-field")
      const button = wrapper.find(".v-btn")
      expect(textFields.length).toBe(3)
      expect(button.exists()).toBe(true)
    })

    it('AnalysisInit component', () => {
      const wrapper = mount(AnalysisInit, {
        localVue,
        vuetify,
        router,
        store
      })

      const inputFile = wrapper.findAll(".v-file-input")
      const button = wrapper.find(".v-btn")
      expect(inputFile.exists()).toBe(true)
      expect(button.exists()).toBe(true)
    })


    it('AnalysisResultTable component', () => {
      let analyses = [
        {
          id: "fafa-4141-daada",
          status: "DONE",
          created_date: new Date(1995,11,17,3,24,0),
          recording_id: "525252afdsfafaf-faffa"
        }
      ]

      let html = 
`<div class="analysis-table-box">
  <div class="v-data-table theme--light">
    <div class="v-data-table__wrapper">
      <table>
        <thead>
          <tr>
            <th>Status</th>
            <th>Data badania</th>
            <th>Nagranie</th>
            <th>Wynik analizy</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>DONE</td>
            <td>1995-12-17 3:24</td>
            <td><a href="/doctor/analysis/525252afdsfafaf-faffa" class="">
                Kliknij by zobaczyć nagranie 🗃️
              </a></td>
            <td><a href="/doctor/analysis/fafa-4141-daada" class="">
                Kliknij by zobaczyć wyniki 🗃️
              </a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>`

      const wrapper = mount(AnalysisResultTable, {
        localVue,
        vuetify,
        router,
        store,
        propsData: {
          analyses: analyses
        }
      })

      const table = wrapper.findAll(".v-data-table")
      expect(table.exists()).toBe(true)
      expect(wrapper.html()).toBe(html)
      
    })


    // it('AnalysisVisualization component', () => {
    //   let patient = {
    //     pesel: "212121",
    //     first_name: "dad",
    //     last_name: "dan",
    //   }
      
    //   let analysis = [
    //     0.1212,
    //     0.1414,
    //     0.41414,
    //     0.1212,
    //     0.1414,
    //     0.41414,
    //     0.1212,
    //     0.1414,
    //     0.41414,
    //     0.1212,
    //     0.1414,
    //     0.41414,
    //   ]

    //   const wrapper = mount(AnalysisVisualization, {
    //     localVue,
    //     vuetify,
    //     router,
    //     store,
    //     propsData: {
    //       patient: patient,
    //       analysisData: analysis
    //     }
    //   })

    //   const chart = wrapper.find(".v-chart")
    //   const cards = wrapper.findAll(".v-card")
    //   expect(chart.exists()).toBe(true)
    //   expect(cards.length).toBe(2)
    // })

    it('LoginForm component', () => {
      const wrapper = mount(LoginForm, {
        localVue,
        vuetify,
        router,
        store
      })

      const textInputs = wrapper.findAll(".v-text-field")
      const buttons = wrapper.findAll(".v-btn")
      expect(textInputs.length).toBe(2)
      expect(buttons.length).toBe(3)
    })

    // it('Navbar component', () => {
    //   const wrapper = mount(Navbar, {
    //     localVue,
    //     vuetify,
    //     router,
    //     store
    //   })

    //   const textInputs = wrapper.findAll(".v-text-field")
    //   const buttons = wrapper.findAll(".v-btn")
    //   expect(textInputs.length).toBe(2)
    //   expect(buttons.length).toBe(3)
    // })

    it('PatientTable component', () => {
      let patients = {
        pesel: "212121",
        first_name: "dad",
        last_name: "dan",
       }
      

      const wrapper = mount(PatientTable, {
        localVue,
        vuetify,
        router,
        store,
        propsData: {
          patientData: patients,
        }
      })

      const card = wrapper.findAll(".v-card")
      expect(card.exists()).toBe(true)
    })


    it('RegisterUserForm component', () => {
      let recordings = [
        {
          id: "fafa-4141-daada",
          filename: "file.wav",
          created_date: new Date(1995,11,17,3,24,0),
          recording_id: "525252afdsfafaf-faffa"
        }
      ]
      

      const wrapper = mount(RegisterUserForm, {
        localVue,
        vuetify,
        router,
        store,
        propsData: {
          recordings: recordings,
        }
      })
      
      const textInputs = wrapper.findAll(".v-text-field")
      const selects = wrapper.findAll(".v-select")
      const buttons = wrapper.findAll(".v-btn")
      expect(textInputs.length).toBe(8)
      expect(selects.length).toBe(2)
      expect(buttons.length).toBe(1)
    })

    it('SearchUser component', () => {
      let recordings = [
        {
          id: "fafa-4141-daada",
          filename: "file.wav",
          created_date: new Date(1995,11,17,3,24,0),
          recording_id: "525252afdsfafaf-faffa"
        }
      ]
      

      const wrapper = mount(SearchUser, {
        localVue,
        vuetify,
        router,
        store,
        propsData: {
          recordings: recordings,
        }
      })
      
      const textInputs = wrapper.findAll(".v-text-field")
      const selects = wrapper.findAll(".v-select")
      const buttons = wrapper.findAll(".v-btn")
      expect(textInputs.length).toBe(5)
      expect(selects.length).toBe(1)
      expect(buttons.length).toBe(1)
    })

})
