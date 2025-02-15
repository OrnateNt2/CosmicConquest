# cosmic_conquest/socketio_server.py

from cosmic_conquest.app import socketio
from flask_socketio import emit, join_room
from cosmic_conquest.engine.game.game import Game
from cosmic_conquest.storyline.story_engine import StoryEngine

# Глобальные объекты (пример)
game_instance = Game()
story_engine = StoryEngine()

@socketio.on('connect')
def handle_connect():
    print("Клиент подключился")

@socketio.on('disconnect')
def handle_disconnect():
    print("Клиент отключился")

@socketio.on('join_game')
def handle_join_game(data):
    room = data.get('room', 'default_room')
    join_room(room)
    emit('player_joined', f"Новый игрок в комнате: {room}", to=room)

@socketio.on('player_move')
def handle_player_move(data):
    move_result = game_instance.process_move(data)
    # Проверяем сюжет
    story_trigger = story_engine.check_story_triggers(game_instance)
    emit('move_update', {
        "move_result": move_result,
        "story_update": story_trigger
    }, broadcast=True)
