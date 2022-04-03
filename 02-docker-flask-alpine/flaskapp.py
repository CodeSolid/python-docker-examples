from flask import Flask

app = Flask(__name__)

@app.route(/)
def flask_main():
    return <h1>Flask is running</h1><p>Awesome, that worked.  Now add more code.</p>