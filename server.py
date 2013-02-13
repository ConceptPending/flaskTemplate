import os
from flask import Flask, render_template, Markup, abort, session

app = Flask(__name__)
app.debug=True

### Hint: Change the below
app.secret_key = r'SuperDuperSecretKey'

# Render and return index.html
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Bing to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)
