from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

decks = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_deck", methods=["GET", "POST"])
def create_deck():
    return render_template("create_deck.html")

if __name__ == "__main__":
    app.run(debug=True)
