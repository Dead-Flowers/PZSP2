
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
 import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
 import { library } from '@fortawesome/fontawesome-svg-core'
 import { faUser, 
  faFlask, 
  faSignOutAlt,
  faUserNurse,
  faUserCircle,
  faUserPlus,
  faPeopleArrows,
  faList,
  faFileAudio,
  faPlusSquare,
  faSquare,
  faCheckSquare,
  faUserShield,
  faUnlockAlt,
  faDigitalTachograph,
 } from '@fortawesome/free-solid-svg-icons'
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
import ECharts from 'vue-echarts';
import { use } from 'echarts/core';

describe('doctor tests', () => {
    const localVue = createLocalVue()
    let vuetify
    let router = Router
    let state
    let store
    library.add(faUser, 
      faFlask,
      faSignOutAlt,
      faUserNurse,
      faUserCircle,
      faUserPlus,
      faPeopleArrows,
      faList,
      faFileAudio,
      faPlusSquare,
      faSquare,
      faCheckSquare,
      faUserShield,
      faUnlockAlt,
      faDigitalTachograph
      )
    localVue.component('font-awesome-icon', FontAwesomeIcon)
    
    use([
      CanvasRenderer,
      BarChart,
      GridComponent,
      TooltipComponent
    ]);

    localVue.component('v-chart', ECharts)

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
          <tr class="">
            <td>DONE</td>
            <td>1995-12-17 03:24</td>
            <td>
              <div><span></span></div>
            </td>
            <td><button type="button" class="v-btn v-btn--is-elevated v-btn--has-bg theme--light v-size--default"><span class="v-btn__content"><i aria-hidden="true" class="v-icon notranslate mdi mdi-note-search theme--light"></i> Pokaż wyniki
          </span></button></td>
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
      expect(buttons.length).toBe(2)
    })

    it('Navbar component', () => {
      const wrapper = mount(Navbar, {
        localVue,
        vuetify,
        router,
        store
      })

      const textInputs = wrapper.findAll(".v-list-item")
      const buttons = wrapper.findAll(".v-btn")
      expect(textInputs.length).toBe(5)
      expect(buttons.length).toBe(1)
    })

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


describe('patient tests', () => {
  const localVue = createLocalVue()
  let vuetify
  let router = Router
  let state
  let store
  library.add(faUser, 
    faFlask,
    faSignOutAlt,
    faUserNurse,
    faUserCircle,
    faUserPlus,
    faPeopleArrows,
    faList,
    faFileAudio,
    faPlusSquare,
    faSquare,
    faCheckSquare,
    faUserShield,
    faUnlockAlt,
    faDigitalTachograph
    )
  localVue.component('font-awesome-icon', FontAwesomeIcon)
  
  use([
    CanvasRenderer,
    BarChart,
    GridComponent,
    TooltipComponent
  ]);

  localVue.component('v-chart', ECharts)

  localVue.use(VueRouter)

  let actions = {
    actionCheckLoggedIn: jest.fn()
  }

  beforeEach(() => {
  state = {
    isLoggedIn: false,
    userType: "patient"
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


  it('Navbar component', () => {
    const wrapper = mount(Navbar, {
      localVue,
      vuetify,
      router,
      store
    })

    const textInputs = wrapper.findAll(".v-list-item")
    const buttons = wrapper.findAll(".v-btn")
    expect(textInputs.length).toBe(3)
    expect(buttons.length).toBe(1)
  })

})

describe('admin tests', () => {
  const localVue = createLocalVue()
  let vuetify
  let router = Router
  let state
  let store
  library.add(faUser, 
    faFlask,
    faSignOutAlt,
    faUserNurse,
    faUserCircle,
    faUserPlus,
    faPeopleArrows,
    faList,
    faFileAudio,
    faPlusSquare,
    faSquare,
    faCheckSquare,
    faUserShield,
    faUnlockAlt,
    faDigitalTachograph
    )
  localVue.component('font-awesome-icon', FontAwesomeIcon)
  
  use([
    CanvasRenderer,
    BarChart,
    GridComponent,
    TooltipComponent
  ]);

  localVue.component('v-chart', ECharts)

  localVue.use(VueRouter)

  let actions = {
    actionCheckLoggedIn: jest.fn()
  }

  beforeEach(() => {
  state = {
    isLoggedIn: false,
    userType: "admin"
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


  it('Navbar component', () => {
    const wrapper = mount(Navbar, {
      localVue,
      vuetify,
      router,
      store
    })

    const textInputs = wrapper.findAll(".v-list-item")
    const buttons = wrapper.findAll(".v-btn")
    expect(textInputs.length).toBe(9)
    expect(buttons.length).toBe(1)
  })

})