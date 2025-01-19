import { createRouter, createWebHistory } from 'vue-router';

import Search from '../components/Search.vue';
import Dashboard from '../components/Dashboard.vue';
import Report from '../components/Report.vue';

const routes = [
    { path: '/', component: Search },
    { path: '/dashboard', component: Dashboard },
    { path: '/search', component: Search },
    { path: '/report', component: Report },
];

const router = createRouter({
    history: createWebHistory(), 
    routes, 
});

export default router;
