import { api } from '@/api';

const defaultState = {
    isLoggedIn: null,
    logInError: false,
    registrationError: false,
    registrationSuccess: false, 
    token: '',
    id: null,
    userID: null,
    username: null,
    first_name: null,
    second_name: null,
    last_name: null,
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
            await context.dispatch("actionLogOut");
            context.commit("openSnackbar", "Problem with logging in")
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
            context.commit("openSnackbar", "Problem with getting user data")
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
                    await context.dispatch("actionCheckApiError", error);
                    context.commit("openSnackbar", "You're not logged in!");
                }
            } else {
                await context.dispatch("actionLogOut");
                context.commit("openSnackbar", "You're not logged in!");
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
        if (payload.response.status === 403) {
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
            await context.dispatch("actionCheckApiError", error);
            context.commit("openSnackbar", "Problem with updating user");
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
            context.commit("openSnackbar", "Problem with registration!");
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
    firstName: (state) => state.first_name,
    secondName: (state) => state.second_name,
    last_name: (state) => state.last_name,
    userType: (state) => state.userType,
    user: (state) => { return {
        userID: null,
        username: state.username,
        first_name: state.first_name,
        second_name: state.second_name,
        last_name: state.last_name,
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
        state.first_name = payload;
    },
    setSecondName(state, payload) {
        state.second_name = payload;
    },
    setLastName(state, payload) {
        state.last_name = payload;
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
    },
    setID(state, payload) {
        state.id = payload
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
    context.commit("setLastName", data.last_name);
    context.commit("setUserType", data.role);
}

const getLocalToken = () => localStorage.getItem('token');

const saveLocalToken = (token) => localStorage.setItem('token', token);

const removeLocalToken = () => localStorage.removeItem('token');
