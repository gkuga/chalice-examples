from chalice import Chalice

app = Chalice(app_name='hello-app')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/hello')
def hello():
    return {'hello': '/hello'}


@app.route('/hello/{key}', methods=['GET', 'PUT'])
def hello2(key):
    request = app.current_request
    if request.method == 'PUT':
        # handle PUT request
        pass
    elif request.method == 'GET':
        # handle GET request
        pass
    return {'key': key}


@app.route('/goodbye')
def goodbye():
    return {'goodbye': '/goodbye'}


@app.route('/goodbye/a')
def goodbye_a():
    return {'goodbye': '/goodbye/a'}


@app.route('/goodbye/a/1')
def goodbye_a1():
    return {'goodbye': '/goodbye/a'}


@app.route('/goodbye/a/2')
def goodbye_a2():
    return {'goodbye': '/goodbye/a'}


@app.route('/goodbye/b')
def goodbye_b():
    return {'goodbye': '/goodbye/b'}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
