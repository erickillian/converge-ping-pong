const top_three_names = JSON.parse(document.getElementById('top_three_names').textContent);
const top_three_scores = JSON.parse(document.getElementById('top_three_scores').textContent);

var chart = new Chart(document.getElementById('top_players'), {
    type: 'bar',
    data: {
      labels: [top_three_names[2], top_three_names[0], top_three_names[1]],
      datasets: [{
        label: 'Elo',
        data: [top_three_scores[2], top_three_scores[0], top_three_scores[1]],
        fill: false,
        backgroundColor: ['rgba(255, 159, 64, 0.7)', 'rgba(255, 205, 86, 0.7)', 'rgba(169, 169, 169, 0.7)' ],
        borderColor: ['rgb(255, 159, 64)', 'rgb(255, 205, 86)', 'rgb(169, 169, 169)'],
        borderWidth: 10
      }]
    },
    options: {
        tooltips: {
            enabled: false
        },
        hover: {
            mode: null
        },
        plugins: {
            labels: {
            render: 'image',
            textMargin: 10,
            images: [
                {
                src: 'static/trophy_bronze.png',
                width: 100,
                height: 100
                },
                {
                    src: 'static/trophy_gold.png',
                    width: 100,
                    height: 100 
                },
                {
                src: 'static/trophy_silver.png',
                width: 100,
                height: 100
                },
            ]
            }
        },
        layout: {
            padding: {
            top: 100
            }
        },
        legend: {
            display: false
        },
        scales: {
            xAxes: [{
                
                gridLines: {
                    drawOnChartArea: false,
                    drawBorder: false,
                },
                angleLines: {
                    display: false
                },
                grid: {
                    display: false
                },
                ticks: {
                    display: true,
                    fontSize: 20,
                }
            }],
            yAxes: [{
                gridLines: {
                    drawOnChartArea: false,
                    drawBorder: false,
                },
                angleLines: {
                    display: false
                },
                ticks: {
                    suggestedMin: top_three_scores[2]*0.85,
                    display: false,
                },
                grid: {
                    display: false
                }
            }]
        }
    }
});