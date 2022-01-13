import { api } from '@/api';

const defaultState = {
    isLoggedIn: null,
    logInError: false,
    registrationError: false,
    registrationSuccess: false,
    pesel: null,
    passport_num: null,
    token: '',
    id: null,
    userID: null, // shoud use pesel and passport_num, this left for now so nothing breaks
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
            return true;
        } catch (error) {
            await context.dispatch("actionCheckApiError", error);
            context.commit("openSnackbar", "Problem with getting user data")
        }
        return false;
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
                    const isLoggedIn = await context.dispatch("actionGetMe");
                    context.commit("setLoggedIn", isLoggedIn);
                    if (!isLoggedIn) {
                        await context.dispatch("actionLogOut");
                    }
                } catch (error) {
                    await context.dispatch("actionCheckApiError", error);
                    context.commit("openSnackbar", "Nie jesteś zalogowany!");
                }
            } else {
                await context.dispatch("actionLogOut");
                context.commit("openSnackbar", "Nie jesteś zalogowany!");
            }
        }
    },

    async actionLogOut(context) {
        removeLocalToken();
        context.commit("setToken", '');
        context.commit("setLoggedIn", false);
        context.commit("openSnackbar", "Zostałeś wylogowany");
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
            if (response.data) {
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
    },

    async actionAddNews(context, payload) {
        try {
            const response = await api.addNews(context.state.token, payload);
            if (response.status == 200) {
                context.commit("setRegistrationError", false);
                context.commit("setRegistrationSuccess", true);
                console.log(response);
            } else {
                context.commit("setRegistrationError", true);
                context.commit("setRegistrationSuccess", false);
                console.log(response);
            }
        } catch (err) {
            context.commit("setRegistrationError", true);
            context.commit("setRegistrationSuccess", false);
            console.log(err);
            context.commit("openSnackbar", "Problem with registration!");
        }
    },

    async actionUpdateNews(context, payload) {
        try {
            const body = {
                title: payload.title,
                description: payload.description
            }
            const response = await api.updateNewsById(context.state.token, payload.id, body);
            if (response.status == 200) {
                context.commit("setRegistrationError", false);
                context.commit("setRegistrationSuccess", true);
                console.log(response);
            } else {
                context.commit("setRegistrationError", true);
                context.commit("setRegistrationSuccess", false);
                console.log(response);
            }
        } catch (err) {
            context.commit("setRegistrationError", true);
            context.commit("setRegistrationSuccess", false);
            console.log(err);
            context.commit("openSnackbar", "Problem with registration!");
        }
    },

    async actionRemoveNews(context, newsId) {
        try {
            const response = await api.removeNewsById(context.state.token, newsId);
            if (response.status == 200) {
                context.commit("setRegistrationError", false);
                context.commit("setRegistrationSuccess", true);
                console.log(response);
            } else {
                context.commit("setRegistrationError", true);
                context.commit("setRegistrationSuccess", false);
                console.log(response);
            }
        } catch (err) {
            context.commit("setRegistrationError", true);
            context.commit("setRegistrationSuccess", false);
            console.log(err);
            context.commit("openSnackbar", "Problem with registration!");
        }
    },
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
    id: (state) => state.id,
    user: (state) => {
        return {
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
    },
    setPesel(state, payload) {
        state.pesel = payload
    },
    setPassportNum(state, payload) {
        state.passport_num = payload
    }

}

export const userModule = {
    state: defaultState,
    mutations,
    actions,
    getters,
};


const setUserData = (context, data) => {
    context.commit("setID", data.id)
    //TODO set pesel or pass number not userID
    if (data.pesel != null) {
        context.commit("setUserID", data.pesel);
        context.commit("setPesel", data.pesel);
    }
    else {
        context.commit("setUserID", data.passport_num);
        context.commit("setPassportNum", data.passport_num);
    }
    context.commit("setUsername", data.email);
    context.commit("setFirstName", data.first_name);
    context.commit("setSecondName", data.second_name);
    context.commit("setLastName", data.last_name);
    context.commit("setUserType", data.role);
}

export const getLocalToken = () => localStorage.getItem('token');

const saveLocalToken = (token) => localStorage.setItem('token', token);

const removeLocalToken = () => localStorage.removeItem('token');
