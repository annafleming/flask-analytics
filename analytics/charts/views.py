from . import charts


@charts.route('/finished')
def finished():
    return 'Finished the survey charts'
