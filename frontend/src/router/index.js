
import { createRouter, createWebHistory } from "vue-router";

import HomeComponent from '../components/HomeComponent.vue'

const routes = [
    {
        path: '/',
        name :'home',
        component: HomeComponent
    },
    {
        path: '/about',
        name: 'about',
        component: HomeComponent
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router