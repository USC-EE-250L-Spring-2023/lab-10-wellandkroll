import flask
from main import process1, process2

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.jsonify({'message': 'Welcome'})

@app.route('/process1', methods=['POST'])
def route_process1():
    # Get data from request
    data = flask.request.get_json()
    # Call process1 with data
    result = process1(data)

    # Return result as JSON response
    return flask.jsonify(result)

# Route for process2
@app.route('/process2', methods=['POST'])
def route_process2():
    # Get data from request
    data = flask.request.get_json()
    # Call process1 with data
    result = process2(data)

    # Return result as JSON response
    return flask.jsonify(result)
@app.route('/delay', methods=['POST'])
def delay():
    message = flask.request.data
    return message

if __name__ == "__main__":
    app.run(host='172.20.10.2',port=8000)
