var gameId = null;
var isGameOver = false;
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
    isGameOver = false;

    $('[id^=cell-]')
        .removeClass('x')
        .removeClass('o')
        .html('');
    $('#game-message').hide();

    let cpu = $('#game-cpu').val();

    // server will decide if the cpu makes the first move 'x'
    $.post( 'api/games', { cpu1: cpu })
      .done(function( gameData ) {
        gameId = gameData['id'];
        updateGameView(gameData);
        if (!gameData['cpuFirstPlayer']) {
            $('#game-message').html(`&Agrave; vous de commencer`)
                .show()
                .delay(2000)
                .slideUp(200, function () {
                    $(this).hide();
        });
        }
      });
}

function playMove(cell, position) {
    if (cell.hasClass('x') || cell.hasClass('o') || isGameOver) {
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
            gameOver(gameData);
        }
}

function gameOver(gameData) {
    isGameOver = true;

    if (!gameData['winningSide'])
        result = 'fait match nul';
    else if (gameData['cpuFirstPlayer'] && gameData['winningSide'] == 'x')
        result = 'perdu';
    else if (!gameData['cpuFirstPlayer'] && gameData['winningSide'] == 'o')
        result = 'perdu';
    else
        result = 'gagn&eacute';

    $('#game-message').html(`Partie termin&eacute;e, vous avez ${result}!`)
        .show()
        .delay(5000)
        .slideUp(200, function () {
            $(this).hide();
        });
}