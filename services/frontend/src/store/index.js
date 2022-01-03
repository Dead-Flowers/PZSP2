import Vue from 'vue'
import Vuex from 'vuex'
import { userModule } from './user';
import { api } from '@/api';

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
    recordingID: null,
    analysisID: null,
    file: null,
    result: null,
  },
  patients: [],
  snackbarOpen: false,
  snackbarText: "",
}

export const mutations = {
  setPatient(state, patient) {
    state.currentPatient = patient;
  },
  setAnalysisFile(state, file) {
    state.analysis.file = file;
  },
  setAnalysisResult(state, result) {
    state.analysis.result = result;
  },
  setPatients(state, patients) {
    state.patients = patients;
  },
  setRecordingID(state, recordingID) {
    state.analysis.recordingID = recordingID;
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
  //! those are initial implementation, change when implementing real feature
  //TODO: change email if needed
  // async getPatient(context, email) {
  //   let patient = await api.getPatient(context.state.user.token, email); // yeah this doesn't work rn 
  //   context.commit("setPatient", patient);
  // },
  // async createPatient(context, patient) {
  //   await api.createPatient(context.state.user.token, patient);
  //   await context.dispatch('getPatient', patient.email); // is this needed ?
  // },
  // async getPatients(context) {
  //   let patients = await api.getUsers()
  //   context.commit('setPatients', patients.data);
  // },
  async startAnalysis(context){
    try {
      let response = await api.startAnalysis(context.state.user.token ,context.state.analysis.recordingID);
      context.commit("setAnalysisID", response.data);
    } catch (e) {
      await context.dispatch("actionCheckApiError", e);
      context.commit("openSnackbar", "Problem with uploading file!");
    }
  },
  async getAnalysisResults(context) {
    let statusCode = 404;
    let data = [];
    let response;
    while (statusCode != 200)
    {
      response = await api.getFrames(context.state.user.token, context.state.analysis.analysisID).catch(e => {
        statusCode = e.status
      })
      if (response !== undefined) {
        statusCode = response.status
      }
      await sleep(200);
    }

    for(const element of response.data)
    {
      data.push(element.probability)
    }
    context.commit("setAnalysisResult", data)
  },

  async uploadFile (context, payload) {
    try {
      let formData = new FormData();
      formData.append('file_in', context.state.analysis.file);
      let response = await api.uploadFile(context.state.user.token, formData, payload.patientID)
      context.commit("setRecordingID", response.data)
      
      response = await api.startAnalysis(context.state.user.token ,context.state.analysis.recordingID)
      context.commit("setAnalysisID", response.data)
    } catch (e) {
      await context.dispatch("actionCheckApiError", e);
      context.commit("openSnackbar", "Problem with uploading file!");
    }
  } 
}

export const getters =  {
  getCurrentPatient: state => state.currentPatient,
  getAnalysisFile: state => state.analysis.file,
  getAnalysisResult: state => state.analysis.result,
  getPatients: state => state.patients,
  getAnalysisID: state => state.analysis.analysisID,
  analysisStarted: state => state.analysis.analysisID == null ? true : false,
  openSnackbar(state, text) {
    state.snackbarOpen = true;
    state.snackbarText = text;
  },
  closeSnackbar(state) {
    state.snackbarOpen = false;
  },
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


function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}