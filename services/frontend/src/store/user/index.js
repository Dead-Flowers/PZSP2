import { api } from '@/api';

const defaultState = {
    isLoggedIn: null,
    logInError: false,
    registrationError: false,
    registrationSuccess: false, 
    token: '',
    userID: null,
    username: null,
    firstName: null,
    secondName: null,
    surName: null,
    userType: null,
  };
  
  export const actions = {
    async actionLogIn(context, payload) {
        try {
            console.log(payload)
            const response = await api.logIn(payload.username, payload.password)
            const token = response.data.access_token;
            if (token) {
                saveLocalToken(token);
                context.commit("setToken", token);
                context.commit("setLoggedIn", true)
                context.commit("setLogInError", false)
                await context.dispatch("actionGetMe"); 
            } else {
                await context.dispatch("actionLogOut");
            }
        } catch (err) {
            context.commit("setLoggedIn", false)
            context.commit("setLogInError", true)
            console.log(err);
            await context.dispatch("actionLogOut");
        }
    },

    async actionGetMe(context) {
        try {
            const response = await api.getMe(context.state.token)
            if (response.data) {
                context.commit("setUserID", response.data.id);
                context.commit("setUsername", response.data.email);
                context.commit("setFirstName", response.data.first_name);
                context.commit("setSecondName", response.data.second_name);
                context.commit("setSurName", response.data.last_name);
                context.commit("setUserType", response.data.role);                
            }
        } catch (error) {
            await context.dispatch("actionCheckApiError", error);
        }
    },

    async actionCheckLoggedIn(context) {
        if (!context.state.isLoggedIn) {
            let token = context.state.token;
            if (!token) {
                const localToken = getLocalToken();
                if (localToken) {
                    context.commit("setToken", localToken);
                    token = localToken;
                }
            }
            if (token) {
                try {
                    await context.dispatch("actionGetMe");
                    context.commit("setLoggedIn", true)
                } catch (error) {
                    await context.dispatch("actionLogOut");
                }
            } else {
                await context.dispatch("actionLogOut");
            }
        }
    },

    async actionLogOut(context) {
        removeLocalToken();
        context.commit("setToken", '');
        context.commit("setLoggedIn", false);
    },

    async actionCheckApiError(context, payload) {
        if (payload.response.status === 401) {
            await context.dispatch("actionLogOut");
        }
    },

    async actionRegister(context, payload) {
        try {
            const response = await api.createUser(context.state.token, payload)
            if (response.status == 200) {
                context.commit("setRegistrationError", false)
                context.commit("setRegistrationSuccess", true)
                console.log(response);
            } else {
                context.commit("setRegistrationError", true)
                context.commit("setRegistrationSuccess", false)
                console.log(response);
            }
        } catch (err) {
            context.commit("setRegistrationError", true)
            context.commit("setRegistrationSuccess", false)
            console.log(err);
        }
      }
    }

  export const getters = {
    loginError: (state) => state.logInError,
    dashboardMiniDrawer: (state) => state.dashboardMiniDrawer,
    token: (state) => state.token,
    isLoggedIn: (state) => state.isLoggedIn,
    username: (state) => state.username,
    email: (state) => state.username,
    firstName: (state) => state.firstName,
    secondName: (state) => state.secondName,
    surName: (state) => state.surName,
    userType: (state) => state.userType,
    user: (state) => { return {
        userID: null,
        username: state.username,
        firstName: state.firstName,
        secondName: state.secondName,
        surName: state.surName,
        userType: state.userType,
        }
    },
    registrationError: (state) => state.registrationError,
    registrationSuccess: (state) => state.registrationSuccess,
    }
 
  export const mutations = {
    setToken(state, payload) {
        state.token = payload;
    },
    setUsername(state, payload) {
        state.username = payload
    },
    setUserID(state, payload) {
        state.userID = payload
    },
    setLoggedIn(state, payload) {
        state.isLoggedIn = payload;
    },
    setLogInError(state, payload) {
        state.logInError = payload;
    },
    setFirstName(state, payload) {
        state.firstName = payload;
    },
    setSecondName(state, payload) {
        state.secondName = payload;
    },
    setSurName(state, payload) {
        state.surName = payload;
    },
    setRegistrationError(state, payload) {
        state.registrationError = payload;
    },
    setRegistrationSuccess(state, payload) {
        state.registrationSuccess = payload;
    },
    setUserType(state, payload) {
        state.userType = payload
    },
    resetRegistration(state) {
        state.registrationSuccess = false;
        state.registrationError = false;
    }

  }

  export const userModule = {
    state: defaultState,
    mutations,
    actions,
    getters,
  };


const getLocalToken = () => localStorage.getItem('token');

const saveLocalToken = (token) => localStorage.setItem('token', token);

const removeLocalToken = () => localStorage.removeItem('token');
