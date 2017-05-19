import Vue from 'vue';
import axios from 'axios';

window.axios = axios;

new Vue({
    el: '#app',
    data: {
        item: 'Testing vue'
    }
})