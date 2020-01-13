$(function () {
    $('#simulation-start').click(function () {
        startSimulations();
    });
});

function startSimulations() {
    let cpu1 = $('#game-cpu1').val();
    let cpu2 = $('#game-cpu2').val();

    $.post('api/games/simulate', {cpu1: cpu1, cpu2: cpu2})
        .done(function (gamesData) {
            let html = '';
            for (var game in gamesData) {
                var table = '<span class="x">1</span><span class="o">2</span>3<br>456<br>789'
                var row = `<tr><td>${id}</td><td>Xav</td><td>Random</td><td>Random</td><td>Xav</td><td>${table}</td><td>N</td></tr>`;
            }
            $('#simulation-body tr:last').after(html);
        });
}