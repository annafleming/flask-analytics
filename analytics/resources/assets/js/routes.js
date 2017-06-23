import VueRouter from 'vue-router';

let routes = [
    {
        path: '/',
        component : require('./components/Summary')
    },
    {
        path: '/charts/finished_survey',
        component : require('./components/FinishedSurvey')
    },
    {
        path: '/charts/feedback_type',
        component : require('./components/FeedbackType')
    },
    {
        path: '/charts/completed_survey',
        component : require('./components/CompletedPurpose')
    },
    {
        path: '/charts/website_rating',
        component : require('./components/WebsiteRating')
    },
    {
        path: '/charts/product_rating',
        component : require('./components/ProductRating')
    },
    {
        path: '/responses/:name',
        component : require('./components/SurveyResponses'),
    },
    {
        path: '/responses/:name/:id',
        component : require('./components/SurveyResponseView'),
    },

];

export default new VueRouter({
    routes
});
