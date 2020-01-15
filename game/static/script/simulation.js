$(function () {
    $('#simulation-start').click(function () {
        $('tr.added').remove();
        startSimulations();
    });
});

function startSimulations() {
    let elemCpu1 = $('#game-cpu1');
    let elemCpu2 = $('#game-cpu2');
    let cpu1 = elemCpu1.find("option:selected").text();
    let cpu2 = elemCpu2.find("option:selected").text();

    $.post('api/games/runSimulation', {cpu1: elemCpu1.val(), cpu2: elemCpu2.val()})
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
                let first = cpu1;
                let second = cpu2;
                if (!game['cpuFirstPlayer']) {
                    first = cpu2;
                    second = cpu1;
                }
                if (game['winningSide']) {
                    winner = game['winningSide'] === 'x' ? first : second;
                    looser = game['winningSide'] === 'o' ? first : second;
                }
                errored = game['gameOver'] ? 'Non' : 'Oui'
                let columns = [game['id'], winner, looser, first, second, board.join(''), errored];
                html += ('<tr class="added"><td>' + columns.join('</td><td>') + '</td></tr>')
            }
            $('#simulation-body tr:last').after(html);
        });
}