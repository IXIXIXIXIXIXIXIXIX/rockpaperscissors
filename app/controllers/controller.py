from app import app
from flask import render_template, request, redirect
from app.models.player import Player, Robot
from app.models.game_assets import game, players, acceptable_answers, add_player 
from app.models.robot_name_chooser import robot_name_chooser

@app.route('/')
def index():
	return render_template('index.html')
	# Change this route, obviously

@app.route('/register_player')
def register_player():

	players.clear()
	game.classic_game()

	return render_template('register_player.html', player_one=True)

@app.route('/register_player', methods=['POST'])
def create_player():

	# Check if the user has chosen extended game
	if len(players) == 0 and request.form['game_type'] == "extended":
		game.extended_game()
	
	add_player(Player(request.form['name']))

	# Create human player 2 on second time round
	if request.form['num_players'] == "two":
		return render_template('register_player.html', player_one=False)

	# Create robot player 2 if selected
	if len(players) < 2:
		add_player(Robot(robot_name_chooser(), game.acceptable_answers))

	
	extended = True if len(game.acceptable_answers) != 3 else False
	vs_robot = True if isinstance(players[1], Robot) else False

	return render_template('play.html', player1=players[0], player2=players[1],
		active_player="player1", extended=extended, answers=game.acceptable_answers, vs_robot=vs_robot)


@app.route('/submit', methods=['POST'])
def submit():

	if request.form['player'] == "player1":
		players[0].choose(request.form['p1_choice'])
		
		if isinstance(players[1], Robot):
			players[1].choose()

			result = game.play(players[0], players[1])

			p1_choice = players[0].choice
			p2_choice = players[1].choice

			players[0].reset()
			players[1].reset()

			return render_template('/result.html', player1=players[0], player2=players[1],
			p1_choice=p1_choice, p2_choice=p2_choice, result=result)

		else:
			extended = True if len(game.acceptable_answers) != 3 else False
			vs_robot = True if isinstance(players[1], Robot) else False

			return render_template('play.html', player1=players[0], player2=players[1],
				active_player="player2", extended=extended, answers=game.acceptable_answers, vs_robot=vs_robot)

	else:
			players[1].choose(request.form['p2_choice'])
			result = game.play(players[0], players[1])

			p1_choice = players[0].choice
			p2_choice = players[1].choice

			players[0].reset()
			players[1].reset()

			return render_template('/result.html', player1=players[0], player2=players[1],
				p1_choice=p1_choice, p2_choice=p2_choice, result=result)


@app.route('/new_round')
def new_round():

		extended = True if len(game.acceptable_answers) != 3 else False
		vs_robot = True if isinstance(players[1], Robot) else False
		return render_template('play.html', player1=players[0], player2=players[1],
			active_player="player1", extended=extended, answers=game.acceptable_answers, vs_robot=vs_robot)


@app.route('/end')
def end():

	if players[0].score > players[1].score:
		res_string_1 = f"{players[0].name} wins!"

	elif players[1].score > players[0].score:
		res_string_1  = f"{players[1].name} wins!"
	else:
		res_string_1 = "No Overall Winner!"

	res_string_2 = f"{players[0].name} won {players[0].score} rounds."
	res_string_3 = f"{players[1].name} won {players[1].score} rounds."
	
	# Reset game and clear out players
	game.classic_game()
	players.clear()

	return render_template('end.html', res_string_1=res_string_1, res_string_2=res_string_2, res_string_3=res_string_3)