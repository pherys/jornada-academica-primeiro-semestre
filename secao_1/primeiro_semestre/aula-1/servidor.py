
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def ola_jardim():

    return "Nosso Jardim (API) está funcionando!"

if __name__ == "__main__":
    app.run(debug=True)
