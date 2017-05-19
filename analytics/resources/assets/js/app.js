import Vue from 'vue';
import axios from 'axios';
import router from './routes';
import VueRouter from 'vue-router';


window.Vue = Vue;
window.axios = axios;
Vue.use(VueRouter);


new Vue({
    el: '#app',
    router: router,
    delimiters: ['[[',']]']
})
