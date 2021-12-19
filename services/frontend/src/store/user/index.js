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
    surname: null,
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
                setUserData(context, response.data)                
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
        console.log(payload)
        if (payload.response.status === 401) {
            await context.dispatch("actionLogOut");
        }
    },

    async actionUpdateMe(context, payload) {
        try {
            const response = await api.updateMe(context.state.token, payload);
            if(response.data) {
                setUserData(context, response.data)
            }
        } catch (error) {
            //TODO: better error handling 
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
    surname: (state) => state.surname,
    userType: (state) => state.userType,
    user: (state) => { return {
        userID: null,
        username: state.username,
        firstName: state.firstName,
        secondName: state.secondName,
        surname: state.surname,
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
        state.surname = payload;
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


const setUserData = (context, data) => {
    context.commit("setUserID", data.id);
    context.commit("setUsername", data.email);
    context.commit("setFirstName", data.first_name);
    context.commit("setSecondName", data.second_name);
    context.commit("setSurName", data.last_name);
    context.commit("setUserType", data.role);
}

const getLocalToken = () => localStorage.getItem('token');

const saveLocalToken = (token) => localStorage.setItem('token', token);

const removeLocalToken = () => localStorage.removeItem('token');
