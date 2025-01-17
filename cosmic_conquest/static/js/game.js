// cosmic_conquest/static/js/game.js

document.addEventListener("DOMContentLoaded", () => {
    const socket = io();
  
    socket.on('connect', () => {
      console.log("Socket.IO connected");
      socket.emit('join_game', { room: 'galaxy_room' });
    });
  
    socket.on('player_joined', (message) => {
      console.log("[Chat] " + message);
    });
  
    socket.on('move_update', (data) => {
      console.log("Move result:", data.move_result);
      if (data.story_update) {
        console.log("Story updated:", data.story_update);
        // Можем обновить интерфейс, показать всплывающее окно сюжета и т.д.
      }
    });
  
    // Пример: отправляем фейковый ход
    function testMove() {
      socket.emit('player_move', {
        playerId: "Player1",
        move: "use_card",
        cardId: 3
      });
    }
  
    // Можно привязать кнопку "Сделать ход" в HTML
    // document.getElementById('make-move-btn').onclick = testMove;
  });
  