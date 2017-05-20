import VueRouter from 'vue-router';

let routes = [
    {
        path: '/',
        component : require('./components/Summary')
    },
    {
        path: '/finished_survey',
        component : require('./components/FinishedSurvey')
    },
    {
        path: '/feedback_type',
        component : require('./components/FeedbackType')
    },
    {
        path: '/completed_survey',
        component : require('./components/CompletedPurpose')
    },
    {
        path: '/website_rating',
        component : require('./components/WebsiteRating')
    },
    {
        path: '/product_rating',
        component : require('./components/ProductRating')
    },
];

export default new VueRouter({
    routes
});
