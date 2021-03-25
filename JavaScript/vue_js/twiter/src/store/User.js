// User state module
export const UserModule = {
    namespaced: true,  // allows name state modules

    state: {
        user: null // initialized as null on app start up
    },

    mutations: {
        SET_USER(state, user) {
            state.user = user
        }
    },

    actions: {
        setUser({ commit }, user) {
            commit('SET_USER', user)
        }
    }
}
