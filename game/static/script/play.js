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

    let cpu = $('')
    $.post( 'api/games', { cpu1: 'center' })
      .done(function( data ) {
        gameId = data['id'];
        console.dir(data);
      });

    // todo contact server to start the game
    // server will decide if the player makes the first move 'x' or not
}

function playMove(cell, position) {
    if (cell.hasClass('x') || cell.hasClass('o')) {
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