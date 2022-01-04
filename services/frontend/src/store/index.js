import Vue from 'vue'
import Vuex from 'vuex'
import { userModule } from './user';

Vue.use(Vuex)

// tutorial for what i know
// commit is for mutations, mutations are synchronous
// dispatch is for actions, actions are asynchronous
// don't know much about modules

const state = {
  //TODO: think it over 
  currentPatient: {
    patientIdType: 'pesel',
    pesel: "0123456789",
    first_name: "wait for fetch",
    second_name: "wait for fetch",
    last_name: "wait fo fetch",
  },
  analysis: {
    analysisID: null,
  },
  snackbarOpen: false,
  snackbarText: "",
}

export const mutations = {
  setPatient(state, patient) {
    state.currentPatient = patient;
  },
  setAnalysisID(state, id) {
    state.analysis.analysisID = id;
  },
  openSnackbar(state, text) {
    state.snackbarOpen = true;
    state.snackbarText = text;
  },
  closeSnackbar(state) {
    state.snackbarOpen = false;
  }
}

export const actions = {
}

export const getters =  {
  getCurrentPatient: state => state.currentPatient,
  getPatients: state => state.patients,
  getAnalysisID: state => state.analysis.analysisID,
  analysisStarted: state => state.analysis.analysisID == null ? true : false,
  isSnackbarOpened: (state) => state.snackbarOpen,
  snackbarText: (state) => state.snackbarText,
}

export default new Vuex.Store({
  state,
  mutations,
  actions,
  modules: {
    user: userModule
  },
  getters,
})