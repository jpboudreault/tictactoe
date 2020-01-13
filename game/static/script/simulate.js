$(function () {
    $('#simulation-start').click(function () {
        startSimulations();
    });
});

function startSimulations() {
    var id = Math.floor(Math.random() * 100);
    var table = '<span class="x">1</span><span class="o">2</span>3<br>456<br>789'
    var row = `<tr><td>${id}</td><td>Xav</td><td>Random</td><td>Random</td><td>Xav</td><td>${table}</td><td>N</td></tr>`;
    $('#simulation-body tr:last').after(row);
}