import Vue from 'vue'
import Vuex from 'vuex'
import { userModule } from './user';
import { api } from '@/api';

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
      recordingID: null,
      analysisID: null,
      file: null,
      result: null,
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
    },
    setRecordingID(state, recordingID) {
      state.analysis.recordingID = recordingID
    },
    setAnalysisID(state, id) {
      state.analysis.analysisID = id
    }
  },
  actions: {
    //! those are initial implementation, change when implementing real feature
    //TODO: change email if needed
    async getPatient(context, email) {
      let patient = await api.getPatient(context.state.user.token, email) // yeah this doesn't work rn 
      context.commit("setPatient", patient)
    },
    async createPatient(context, patient) {
      await api.createPatient(context.state.user.token, patient)
      await context.dispatch('getPatient', patient.email) // is this needed ?
    },
    async getPatients(context) {
      let patients = await api.getUsers()
      context.commit('setPatients', patients.data)
    },
    async startAnalysis(context){
      let response = await api.startAnalysis(context.state.user.token ,context.state.analysis.recordingID)
      context.commit("setAnalysisID", response.data)
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
      console.log(response.data)
      for(const element of response.data)
      {
        data.push(element.probability)
      }
      context.commit("setAnalysisResult", data)
    },
    async uploadFile (context) {
      let formData = new FormData();
      formData.append('file_in', context.state.analysis.file);
      console.log('hui')
      let response = await api.uploadFile(context.state.user.token, formData)
      context.commit("setRecordingID", response.data)
      
      response = await api.startAnalysis(context.state.user.token ,context.state.analysis.recordingID)
      context.commit("setAnalysisID", response.data)
    } 
  },
  modules: {
    user: userModule
  },
  getters: {
    getCurrentPatient: state => state.currentPatient,
    getAnalysisFile: state => state.analysis.file,
    getAnalysisResult: state => state.analysis.result,
    getPatients: state => state.patients,
    getAnalysisID: state => state.analysis.analysisID,
    analysisStared: state => state.analysis.analysisID == null ? true : false,
  }
})


function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}