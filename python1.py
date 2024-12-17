# Simple Python script to print "Hello, GitHub Codespaces! using Flask library"
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, GitHub Codespaces!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

