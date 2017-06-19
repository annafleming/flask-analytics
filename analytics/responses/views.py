from . import responses


@responses.route('/fetch/<name>')
def fetch(name):
    return 'Responses for ' + name
