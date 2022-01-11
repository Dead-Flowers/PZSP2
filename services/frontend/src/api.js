import { default as Axios } from 'axios';
import { API_URL } from "./config";

const axios = Axios.create({
  validateStatus: function(status) {
    return status >= 200 && status < 300;
  },
  baseURL: API_URL
});


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

    return axios.post(`${APISUFFIX}/api/login/access-token`, params);
  },

  async getMe(token) {
    return axios.get(`${APISUFFIX}/api/users/me`, authHeaders(token));
  },

  async updateMe(token, data) {
    return axios.put(`${APISUFFIX}/api/users/me`, data, authHeaders(token));
  },

  async getUsers(token, params) {
    let config = authHeaders(token);
    if (params !== undefined) {
      config['params'] = params;
    }
    return axios.get(`${APISUFFIX}/api/users/`, config);
  },
  async getUser(token, id) {
    return axios.get(`${APISUFFIX}/api/users/${id}`, authHeaders(token));
  },
  async updateUser(token, userId, data) {
    return axios.put(`${APISUFFIX}/api/users/${userId}`, data, authHeaders(token));
  },

  async createUser(token, data) {
    return axios.post(`${APISUFFIX}/api/users/`, data, authHeaders(token));
  },

  async createUserOpen(data) {
    return axios.post(`${APISUFFIX}/api/users/open`, data);
  },

  async uploadFile(token, file, patientID) {
    let config = authHeaders(token);
    config.headers ['Content-Type'] = 'multipart/form-data';
    config["params"] = {};
    config.params["patient_id"] = patientID;
    return axios.post(`${APISUFFIX}/api/analysis/recordings/upload`,
    file,
    config);
  },

  async startAnalysis(token, recordingID) {
      return axios.post(`${APISUFFIX}/api/analysis/recordings/${recordingID}/analyze`, null, authHeaders(token));
  },

  async getAnalysisResults(token, analysisID) {
      return axios.get(`${APISUFFIX}/api/analysis/results/${analysisID}`, authHeaders(token));
  },

  async getFrames(token, analysisID) {
    return axios.get(`${APISUFFIX}/api/analysis/results/${analysisID}/frames`, authHeaders(token));
  },

  async getAnalysis(token, patientID) {
    let config = authHeaders(token);
    config["params"] = {};
    config.params["patient_id"] = patientID;
    return axios.get(`${APISUFFIX}/api/analysis/results`, config);
  },

  async getRecordings(token, patientID) {
    let config = authHeaders(token);
    config["params"] = {};
    config.params["patient_id"] = patientID;
    return axios.get(`${APISUFFIX}/api/analysis/recordings`, config);
  },

  async getRecording(token, recordingID) {
    let config = authHeaders(token);
    return axios.get(`${APISUFFIX}/api/analysis/recordings/${recordingID}`, config);
  },

  downloadRecording(token, recordingID, downloadCallback) {
    return axios.request({
      method: 'post',
      url: `${APISUFFIX}/api/analysis/recordings/${recordingID}/download`,
      ...authHeaders(token),
      responseType: 'arraybuffer',
      onDownloadProgress: downloadCallback
    });
  }
  

};