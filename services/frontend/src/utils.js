import axios from 'axios';

function authHeaders(token) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}

const APISUFFIX = ""

export const api = {
  async logIn(username, password) {
    const params = new URLSearchParams();
    params.append('username', username);
    params.append('password', password);

    return axios.post(`${APISUFFIX}/login/`, params);
  },
  async getUser(token, userID) {
    return axios.get(`${APISUFFIX}/user/${userID}`, authHeaders(token));
  },

  async getUsers(token) {
    return axios.get(`${APISUFFIX}/users`, authHeaders(token));
  },

  async getPatient(token, email) {

  },

  async createPatient(token, patient) {

  },

  async uploadFile(token, file) {
    return axios.post("recordings/upload",
    file,
    {
      headers: {
          'Content-Type': 'multipart/form-data',
          authHeaders(token)
      }
    })
  },

  async startAnalysis(token, recordingID) {
      return axios.post(`${APISUFFIX}/recordings/${recordingID}/analyze`, authHeaders(token))
  },

  async getAnalysisResults(token, analysisID) {
      return axios.get(`${APISUFFIX}/results/${analysisID}`, authHeaders(token))
  }

};