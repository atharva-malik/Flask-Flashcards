from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# Sample data (replace with database later)
decks = {'Test': [{'question': 'Who am i?', 'answer': 'Atharva'}]}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_deck", methods=["GET", "POST"])
def create_deck():
    if request.method == "POST":
        deck_name = request.form["deck_name"]
        decks[deck_name] = []  # Empty list for flashcards
        return redirect(url_for("view_deck", deck_name=deck_name, flag=True))
    return render_template("create_deck.html")

@app.route("/view_deck/<deck_name>/<flag>", methods=["GET", "POST"])
def view_deck(deck_name, flag):
    if deck_name not in decks:
        return "Deck not found!"

    # Handle form submission for adding new cards
    if request.method == "POST":
        try:
            question = request.form["question"]
            answer = request.form["answer"]
            decks[deck_name].append({"question": question, "answer": answer})
            return redirect(url_for("view_deck", deck_name=deck_name))
        except Exception:
            print("Hi", flag, decks)
            if flag == "True":
                return redirect(url_for("view_deck", deck_name=deck_name, flag=False))
            else:
                return redirect(url_for("view_deck", deck_name=deck_name, flag=True))

    # Render template with context
    return render_template("view_deck.html", deck_name=deck_name, deck=decks[deck_name], flag=flag)

if __name__ == "__main__":
    app.run(debug=True)
