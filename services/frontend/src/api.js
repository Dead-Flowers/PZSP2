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

  async uploadFile(token, file) {
    let headers = authHeaders(token);
    headers.headers ['Content-Type'] = 'multipart/form-data';
    return axios.post(`${APISUFFIX}/analysis/recordings/upload`,
    file,
    headers)
  },

  async startAnalysis(token, recordingID) {
      return axios.post(`${APISUFFIX}/analysis/recordings/${recordingID}/analyze`, authHeaders(token))
  },

  async getAnalysisResults(token, analysisID) {
      return axios.get(`${APISUFFIX}/analysis/results/${analysisID}`, authHeaders(token))
  },

  async getFrames(token, analysisID) {
    return axios.get(`${APISUFFIX}/analysis/results/${analysisID}/frames`, authHeaders(token))
  }

};