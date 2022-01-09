
import { createLocalVue, mount } from '@vue/test-utils'
import App from '@/App.vue'
import Vuetify from 'vuetify'
import VueRouter from 'vue-router'
import s from '@/store'
import Welcome from '@/views/common/Welcome.vue'
import { getters } from "@/store/user";
import Vuex from 'vuex'
import Router from "@/router"


describe('App mount layout', () => {
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

    it('mount basic layout', () => {
      const wrapper = mount(App, {
        localVue,
        vuetify,
        router,
        store
      })

      const NavBar = wrapper.findAllComponents({name: 'NavBar'})
      const Welcome = wrapper.findAllComponents({name: 'Welcome'})
      expect(NavBar.exists()).toBe(false)
      expect(Welcome.exists()).toBe(true)
    })

})
