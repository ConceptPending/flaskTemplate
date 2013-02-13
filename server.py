import os
from flask import Flask, render_template, Markup, abort, request, Response
from functools import wraps

app = Flask(__name__)
app.debug=True

def check_auth(username, password):
    #insert code to check against userdb here
    return username == 'guest' and password == 'secret'
    
def authenticate():
    return Response(
    'You must be logged in to continue.', 401,
    {'WWW-Authenticate': 'Basic realm="Please log in"'})
    
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

# Render and return index.html
@app.route('/')
@requires_auth
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Bing to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
