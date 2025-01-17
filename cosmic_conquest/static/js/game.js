document.addEventListener("DOMContentLoaded", () => {
    const socket = io();
  
    socket.on('connect', () => {
      console.log("[SocketIO] Connected");
      socket.emit('join_game', { room: 'galaxy_room' });
    });
  
    socket.on('player_joined', (message) => {
      console.log("[Chat]", message);
    });
  
    socket.on('move_update', (data) => {
      console.log("[Move Update]", data.move_result);
      if (data.story_update) {
        console.log("[Story Update]", data.story_update);
        // Можно обновить UI, показать всплывающий диалог и т.д.
      }
    });
  
    // Пример отправки тестового хода
    function makeTestMove() {
      socket.emit('player_move', {
        playerId: "Player1",
        move: "use_card",
        cardId: 3
      });
    }
  
    // Можно привязать к кнопке в HTML (если она есть)
    // document.getElementById('some-button').onclick = makeTestMove;
  });
  