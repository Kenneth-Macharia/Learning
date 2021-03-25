// Base application state module
import { createStore } from 'vuex' // install vuex@next (v4 for vue3)
import { UserModule } from './User'

export default createStore({
    // application global properties
    state: {},

    // These are functions that effect the STATE. Are declared in CAPS always
    mutations: {},

    // These are functions called throughout the app to accomplish any task including running mutations
    actions: {},

    // These are namespaced state modules
    modules: {
        User:UserModule
    }
})
