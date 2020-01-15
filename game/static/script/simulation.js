$(function () {
    $('#simulation-start').click(function () {
        startSimulations();
    });
});

function startSimulations() {
    let cpu1 = $('#game-cpu1').val();
    let cpu2 = $('#game-cpu2').val();

    $.post('api/games/runSimulation', {cpu1: cpu1, cpu2: cpu2})
        .done(function (gamesData) {
            let html = '';
            // #, Winner, Loser, 1st player, 2nd player, Game, Error
            for (const game of gamesData) {
                let board = [];
                for (let i = 0; i < 9; i++) {
                    let number = game['moves'].indexOf(i) + 1;
                    switch (game['data'][i]) {
                        case ' ':
                            board.push('-');
                            break;
                        case 'x':
                            board.push(`<span class="x">${number}</span>`);
                            break;
                        case 'o':
                            board.push(`<span class="o">${number}</span>`);
                            break;
                    }
                    if (i === 2 || i === 5)
                        board.push('<br>')
                }
                let winner = '-';
                let looser = '-';
                if (game['winningSide']) {
                    winner = game['winningSide'] === 'x' ? cpu1 : cpu2;
                    looser = game['winningSide'] === 'o' ? cpu1 : cpu2;
                }
                let columns = [game['id'], winner, looser, cpu1, cpu2, board.join(''), !game['gameOver']];
                html += ('<tr><td>' + columns.join('</td><td>') + '</td></tr>')
            }
            $('#simulation-body tr:last').after(html);
        });
}