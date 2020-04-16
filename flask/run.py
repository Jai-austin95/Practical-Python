import os
from flask import Flask

app = Flask(__name__ )

@app.route("/")
def index():
    return "Hello, World"

if __name__ == "__main__":
    app.run(host=os.eviron.get("IP"),
            port=int(os.environ.get("port")),
            debug=True)