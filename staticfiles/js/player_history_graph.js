const player_history = JSON.parse(document.getElementById('player_history').textContent);
console.log(player_history);

var top_players_chart = new Chart(document.getElementById('player_history_graph'), {
    type: 'scatter',
    data: {
        datasets: [{
            data: player_history,
            fill: false,
            showLine: true,
            tension: 0,
            pointRadius: 10,
            borderColor: 'black',
        }], 
    },
    options: {
        parsing: {
            xAxisKey: 'time',
            yAxisKey: 'rating',
        },
        tooltips: {
            enabled: true
        },
        legend: {
            display: false
        },
        scales: {
            x: {
                type: 'time',
                // parsing: false,
                time: {
                    unit: 'milisecond'
                },
                displayFormats: {
                    'day': 'MMM DD'
                },
                ticks: {
                    'source': 'auto',
                }
            }
        }
    }
});