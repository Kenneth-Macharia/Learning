import { createRouter, createWebHistory } from "vue-router" // install vue-router@next (v4 for vue3)
import store from '../store'
import Home from '../views/Home.vue'
import UserProfile from '../views/UserProfile.vue'
import AdminPage from '../views/AdminPage.vue'
import { usersObj } from '../assets/users'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home  //normal loading
    },
    {
        path: '/user/:userId',
        name: 'UserProfile',
        component: UserProfile
    },
    {
        path: '/admin',
        name: 'Admin',
        component: AdminPage,
        meta: {
            requiresAdmin: true
        }
    }

    /* lazy loading views:
        component: () => import('path-to-view')
    */
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

// router guards run before or after a routing activity & can be used for pre-routing validation

router.beforeEach(async (to, from, next) => {
    const user = store.state.User.user

    if (!user) {
        // add a user from backend to init the user global state
        // use dispatch to run action
        await store.dispatch('User/setUser', usersObj[0])
    }

    const isAdmin = true
    const requiresAdmin = to.matched.some(record => record.meta.requiresAdmin)

    if (requiresAdmin && !isAdmin) next({ name: 'Home'});
    else next();
})

export default router
