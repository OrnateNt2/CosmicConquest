# cosmic_conquest/routes/main_routes.py

from flask import Blueprint, render_template, request
from cosmic_conquest.engine.game.game import Game
from cosmic_conquest.storyline.story_engine import StoryEngine
from cosmic_conquest.models_db import PlayerDB
from cosmic_conquest.database import db

main_bp = Blueprint('main', __name__)

game_instance = Game()
story_engine = StoryEngine()

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/game')
def game_page():
    if not game_instance.is_started:
        # Для примера создадим пару игроков
        game_instance.add_player("Player1", "Human")
        game_instance.add_player("Player2", "Zorgon")
        game_instance.start_game()
    return render_template('game.html')

@main_bp.route('/story_dialogue', methods=['GET', 'POST'])
def story_dialogue():
    if request.method == 'POST':
        choice = request.form.get("choice")
        if choice:
            story_update = story_engine.choose_branch(choice)
            return render_template('story_dialogue.html', story=story_update)

    current_story = story_engine.get_current_story_segment()
    return render_template('story_dialogue.html', story=current_story)

@main_bp.route('/players')
def list_players():
    """
    Простой пример: Вывести список игроков из БД
    """
    players_db = PlayerDB.query.all()
    return render_template('players.html', players=players_db)
