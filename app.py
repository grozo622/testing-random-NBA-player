# app.py
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def get_player_info(player_name):
    # Function to get player information from a web search
    # You can replace this with more advanced web scraping logic
    url = f"https://www.google.com/search?q={player_name}+NBA+stats"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract relevant information from the HTML using BeautifulSoup
    # This is a simplified example, you may need to customize it based on the actual structure of the search results
    player_image = soup.find('img')['src']
    player_stats = soup.find('div', class_='BNeawe iBp4i AP7Wnd').get_text()
    return player_image, player_stats

@app.route("/")
def index():
    return render_template("index.html", title="NBA Player Information")

@app.route("/player", methods=['POST'])
def display_player():
    player_name = request.form['player_name']
    player_image, player_stats = get_player_info(player_name)
    return render_template("player.html", title="NBA Player Information", player_name=player_name, player_image=player_image, player_stats=player_stats)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
