from flask import Flask,render_template
import socket

app = Flask(__name__)

@app.route("/")
def index():
    return ('server up and running')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
