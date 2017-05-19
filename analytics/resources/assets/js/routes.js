import VueRouter from 'vue-router';

let routes = [
    {
        path: '/',
        component : require('./components/Summary')
    }
];

export default new VueRouter({
    routes
});
