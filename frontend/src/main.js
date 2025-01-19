import * as Vue from 'vue';
import App from './App.vue';
import './assets/style.css';
import router from './routers/router';

const app = Vue.createApp(App);
app.use(router);
app.mount('#app');
export { app };

