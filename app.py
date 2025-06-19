from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Azure Python Web App!"

if __name__ == "__main__":
    app.run()
