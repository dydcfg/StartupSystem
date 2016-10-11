from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return str(int(time.time()*1000))

if __name__ == "__main__":
    app.run()
