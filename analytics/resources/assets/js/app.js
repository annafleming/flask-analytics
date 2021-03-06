import Vue from 'vue';
import axios from 'axios';
import router from './routes';
import VueRouter from 'vue-router';
import Chart from 'chart.js';
import Moment from 'moment';

window.Vue = Vue;
window.axios = axios;
window.Chart = Chart;
window.Event = new Vue();
window.Moment = Moment;
Vue.use(VueRouter);

import Refresh from './components/Refresh';

new Vue({
    el: '#app',
    router: router,
    components: { Refresh },
    delimiters: ['[[',']]']
})
