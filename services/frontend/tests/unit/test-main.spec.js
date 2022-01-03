
import { createLocalVue, mount } from '@vue/test-utils'
import App from '@/App.vue'
import Vuetify from 'vuetify'
import VueRouter from 'vue-router'
import s from '@/store'
import Welcome from '@/views/common/Welcome.vue'

describe('App mount layout', () => {
    const localVue = createLocalVue()
    let vuetify
    let router
    localVue.use(VueRouter)

    const $store = s;
    const routes = [
        {
            path: '/',
            name: 'WelcomePage',
            component: Welcome
          },
       ]

    beforeEach(() => {
    vuetify = new Vuetify()
    router = new VueRouter({ routes })
    })

    it('mount basic layout', () => {
      const wrapper = mount(App, {
        localVue,
        vuetify,
        router,
        mocks: {
          $store,
        },
      })

      const NavBar = wrapper.findAllComponents({name: 'NavBar'})
      const Welcome = wrapper.findAllComponents({name: 'Welcome'})
      expect(NavBar.exists()).toBe(false)
      expect(Welcome.exists()).toBe(true)
    })

})


describe('App mount layout', () => {
  const localVue = createLocalVue()
  let vuetify
  let router
  localVue.use(VueRouter)

  const $store = s;
  const routes = [
      {
          path: '/',
          name: 'WelcomePage',
          component: Welcome
        },
     ]

  beforeEach(() => {
    vuetify = new Vuetify()
    router = new VueRouter({ routes })
    store
  })

  it('mount basic layout', () => {
    const wrapper = mount(App, {
      localVue,
      vuetify,
      router,
      mocks: {
        $store,
      },
    })

    const NavBar = wrapper.findAllComponents({name: 'NavBar'})
    const Welcome = wrapper.findAllComponents({name: 'Welcome'})
    expect(NavBar.exists()).toBe(false)
    expect(Welcome.exists()).toBe(true)
  })

})