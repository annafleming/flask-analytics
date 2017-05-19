let mix = require('laravel-mix').mix;


mix.js('analytics/resources/assets/js/app.js', 'analytics/static/js')
.sass('analytics/resources/assets/sass/app.scss', 'analytics/static/css');