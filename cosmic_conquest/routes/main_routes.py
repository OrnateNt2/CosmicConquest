# cosmic_conquest/routes/main_routes.py

from flask import Blueprint, render_template, request
from cosmic_conquest.engine.game.game import Game
from cosmic_conquest.storyline.story_engine import StoryEngine

main_bp = Blueprint('main', __name__)

# Для примера создадим "одиночные" глобальные объекты
game = Game()
story_engine = StoryEngine()

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/game')
def game_page():
    # Если игра не запущена, инициализируем
    if not game.is_started:
        game.add_player("Player1", "Human")
        game.add_player("Player2", "Zorgon")
        game.start_game()
    return render_template('game.html')

@main_bp.route('/story_dialogue', methods=['GET', 'POST'])
def story_dialogue():
    if request.method == 'POST':
        choice = request.form.get("choice")
        if choice:
            story_update = story_engine.choose_branch(choice)
            return render_template('story_dialogue.html', story=story_update)

    # Просто выводим текущий сегмент
    current_story = story_engine.get_current_story_segment()
    return render_template('story_dialogue.html', story=current_story)
