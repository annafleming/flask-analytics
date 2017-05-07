var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('styles', function() {
    gulp.src('analytics/source/sass/style.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('analytics/static/css'));
});

gulp.task('default',function() {
    gulp.watch('analytics/source/sass/style.scss',['styles']);
});