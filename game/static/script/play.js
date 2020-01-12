var gameId = null;
$(function () {
    $('#game-start').click(function () {
        startGame();
    });
    $('[id^=cell-]').click(function () {
        let position = $(this).attr('id').replace('cell-', '');
        playMove($(this), position);
    });
});

function startGame() {
    gameId = null;
    $('[id^=cell-]')
        .removeClass('x')
        .removeClass('o')
        .html('');

    let cpu = $('#game-cpu').val();

    // server will decide if the cpu makes the first move 'x'
    $.post( 'api/games', { cpu1: cpu })
      .done(function( gameData ) {
        gameId = gameData['id'];
        updateGameView(gameData);
      });
}

function playMove(cell, position) {
    if (cell.hasClass('x') || cell.hasClass('o')) {
        console.log(`invalid move: ${position}`);
        return;
    }

    $.post( `api/games/${gameId}/move`, { move: position })
      .done(function( gameData ) {
        updateGameView(gameData);
      });
}

function updateGameView(gameData) {
        gameData['moves'].forEach(function (move, index) {
            let side = index % 2 == 0 ? 'x' : 'o';
            $(`[id^=cell-${move}]`)
                .addClass(side)
                .html(side);
        });
        if (gameData['gameOver']) {
            gameOver();
        }
}

function gameOver() {
    result = 'perdu';
    $('#game-message').html(`Partie termin&ecute;e, vous avez ${result}!`)
        .show()
        .delay(5000)
        .slideUp(200, function () {
            $(this).hide();
        });
}