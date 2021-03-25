import { createApp } from 'vue'
import router from './router'
import App from './App.vue'
import store from './store'

// mount App parent component to the #app div
createApp(App).use(store).use(router).mount('#app')
