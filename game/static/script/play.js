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
    // server will decide if the player makes the first move 'x' or not
    $.post( 'api/games', { cpu1: cpu })
      .done(function( data ) {
        gameId = data['id'];
        data['moves'].forEach(function (move, index) {
            let side = index % 2 == 0 ? 'x' : 'o';
            $(`[id^=cell-${move}]`)
                .addClass(side)
                .html(side);
        });
      });
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