from flask import Flask, jsonify, request, render_template
import flask
import requests
import store
import os
import random
from flask_cors import CORS
import game1
#dddd

app = Flask(__name__, static_url_path='', static_folder='foodapp/build', template_folder='templates')
CORS(app)

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route("/login", methods=["POST"])
def indexlogin():
    userName = request.args.get("username")
    return app.send_static_file('index.html')

@app.route("/login", methods=["GET"])
def Userlogin():
    return app.send_static_file('index.html')

<<<<<<< HEAD
@app.route("/intro", methods=["GET"])
def UserIntro():
    return app.send_static_file('index.html')

# game 1 backend
options = {
    "A": "https://northcoastmmc.org/wp-content/uploads/2010/04/29748_394524522711_695967711_4377087_2275354_n.jpg",
    "B": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Humpback_Whale_underwater_shot.jpg/300px-Humpback_Whale_underwater_shot.jpg",
    "C": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUsGolBuFlC7LNoSmhsnG_ZWgzeM_C_40yyQ&usqp=CAU",
    "D": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwqTk3fgbj-asLnwgd3LiIRYaPGV2aTtO5MQ&usqp=CAU"
}
=======
>>>>>>> victro_try1

options = {}
correct_answer = ''
idx = 0


@app.route('/game')
def game():
    global options
    global correct_answer
    global idx
    game = game1.Game1()
    options, correct_answer, idx = game.game1_backend()
    return render_template('index2.html', options=options)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    global options
    global correct_answer
    global idx
    if flask.request.method == 'POST':
        user_answer = request.form['answer']
        result = "Correct!" if user_answer == correct_answer else "Wrong!"
        idx_dict = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}
        return jsonify({'result': result, 'answer': idx_dict[idx+1]})
    else:
        return correct_answer


if __name__ == "__main__":
    app.run(debug=True)