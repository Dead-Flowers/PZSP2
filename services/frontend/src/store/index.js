import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

// tutorial for what i know
// commit is for mutations, mutations are synchronous
// dispatch is for actions, actions are asynchronous
// don't know much about modules

export default new Vuex.Store({
  state: {
    currentPatient: {
      patientIdType: 'pesel',
      patientId: null,
      firstName: null,
      secondName: null,
      surname: null,
    },
    analysis: {
      file: null,
      result: null
    },
    patients: []
  },
  mutations: {
    setPatient(state, patient) {
      state.currentPatient = patient;
    },
    setAnalysisFile(state, file) {
      state.analysis.file = file
    },
    setAnalysisResult(state, result) {
      state.analysis.result = result
    },
    setPatients(state, patients) {
      state.patients = patients
    }
  },
  actions: {
    //TODO: change email if needed
    async getPatient(state, email) {
      let patient = await axios.get('user/'+email) // yeah this doesn't work rn 
      state.commit("setPatient", patient)
    },
    async createPatient(state, patient) {
      await axios.post('user', patient)
      await state.dispatch('getPatient', patient.email) // is this needed ?
    },
    async getPatients(state) {
      let patients = await axios.get("users")
      state.commit('setPatients', patients)
    }
  },
  modules: {
  },
  getters: {
    getCurrentPatient: state => state.currentPatient,
    getAnalysisFile: state => state.analysis.file,
    getAnalysisResult: state => state.result,
    getPatients: state => state.getPatients,
  }
})
