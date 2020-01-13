var gameId = null;
var isGameOver = false;

$(function () {
    $('#game-start').click(function () {
        startGame();
    });
    $('[id^=cell-]').click(function () {
        let position = $(this).attr('id').replace('cell-', '');
        playPosition($(this), position);
    });
});

function startGame() {
    gameId = null;
    isGameOver = false;

    // clear the grid & messages
    $('[id^=cell-]')
        .removeClass('x')
        .removeClass('o')
        .html('');
    $('#game-message').hide();

    let cpu = $('#game-cpu').val();

    // call server will decide if the cpu makes the first move 'x'
    $.post('api/games', {cpu1: cpu})
        .done(function (gameData) {
            gameId = gameData['id'];
            updateGameView(gameData);
            if (!gameData['cpuFirstPlayer']) {
                displayMessage(`&Agrave; vous de commencer`, 2000);
            }
        });
}

function playPosition(cell, position) {
    // the game is over or has not started yet, flash the new game button
    if (!gameId || isGameOver) {
        flashNewGameButton();
    }

    // the player clicked an occupied cell
    if (cell.hasClass('x') || cell.hasClass('o') || isGameOver) {
        console.log(`Invalid move: ${position}`);
        return;
    }

    $.post(`api/games/${gameId}/move`, {move: position})
        .done(function (gameData) {
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
        displayGameOver(gameData);
    }
}

function displayGameOver(gameData) {
    isGameOver = true;

    if (!gameData['winningSide'])
        result = 'fait match nul';
    else if (gameData['cpuFirstPlayer'] && gameData['winningSide'] == 'x')
        result = 'perdu';
    else if (!gameData['cpuFirstPlayer'] && gameData['winningSide'] == 'o')
        result = 'perdu';
    else
        result = 'gagn&eacute';

    displayMessage(`Partie termin&eacute;e, vous avez ${result}!`, 5000);
}

function displayMessage(message, delay) {
    $('#game-message').html(message)
        .show()
        .delay(delay * 1000)
        .slideUp(function () {
            $(this).hide();
        });
}

function flashNewGameButton() {
    $('#game-start')
        .addClass('btn-outline-primary')
        .removeClass('btn-primary')
        .delay(150)
        .queue(function () {
            $(this)
                .removeClass('btn-outline-primary')
                .addClass('btn-primary')
                .dequeue();
        });
}