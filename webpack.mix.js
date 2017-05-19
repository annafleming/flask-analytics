let mix = require('laravel-mix').mix;


mix.js('analytics/resources/assets/js/app.js', 'analytics/static/js')
.sass('analytics/resources/assets/sass/app.scss', 'analytics/static/css')
.copy('./node_modules/font-awesome/fonts', 'analytics/static/vendor/fonts')
.copy('./node_modules/font-awesome/css/font-awesome.min.css', 'analytics/static/vendor/font-awesome');