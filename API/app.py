from flask import render_template # Remove: import Flask
from flask_cors import CORS
import connexion

app = connexion.App(__name__, specification_dir="./SPECS")
CORS(app.app)
app.add_api("openapi.yaml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
