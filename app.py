from flask import Flask, render_template
from random import choices

app = Flask(__name__)

def random_nba_player():
    """Returns random NBA player"""
    players = ["Stephen Curry", "Lebron James", "Damian Lillard"]
    return choices(players)

@app.route("/")
def player():
    """Return random player"""
    my_player = random_nba_player()
    return render_template("index.html", title="Random NBA Player", player=my_player)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
