import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

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
    }
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
    }
  },
  actions: {
    //TODO: change email if needed
    getPatient(state, email) {

      
    }

  },
  modules: {
  },
  getters: {
    getCurrentPatient: state => state.currentPatient,
    getAnalysisFile: state => state.analysis.file,
    getAnalysisResult: state => state.result,s
  }
})
