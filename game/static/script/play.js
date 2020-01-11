var gameId = null;
$(function () {
    $('#game-start').click(function () {
        startGame();
    });
    $('[id^=cell-]').click(function () {
        let position = $(this).attr('id').replace('cell-', '');
        playMove(position);
    });
});

function startGame() {
    gameId = null;
    $('[id^=cell-]')
        .removeClass('x')
        .removeClass('o')
        .html('');

    // todo contact server to start the game
    // server will decide if the player makes the first move 'x' or not
}

function playMove(position) {
    if ($(this).hasClass('x') || $(this).hasClass('o')) {
        console.log(`invalid move: ${position}`);
        return;
    }

    // todo contact the server with the move
    // possibly call gameOver()
    $(`#cell-${position}`)
        .html('X')
        .addClass('x');

    $('#game-message')
        .html('Bien jou&eacute;!')
        .show()
        .delay(2000)
        .slideUp(200, function () {
            $(this).hide();
        });
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