const names = JSON.parse(document.getElementById('names').textContent);
const scores = JSON.parse(document.getElementById('scores').textContent);

console.log(names);
console.log(scores);

var all_players_chart = new Chart(document.getElementById('all_players'), {
    type: 'bar',
    data: {
      labels: names,
      datasets: [{
        label: 'Rating',
        data: scores,
        fill: false,
        // backgroundColor: ['rgba(255, 255, 0, 0.7)'],
        // borderColor: ['rgb(255, 255, 0)'],
        borderWidth: 10
      }]
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
    options: {
        tooltips: {
            enabled: true
        },
        hover: {
            mode: true
        },
        plugins: {
            labels: {
                render: 'value',
                textMargin: 10,
                // images: [
                //     {
                //     src: 'static/trophy_bronze.png',
                //     width: 100,
                //     height: 100
                //     },
                //     {
                //         src: 'static/trophy_gold.png',
                //         width: 100,
                //         height: 100 
                //     },
                //     {
                //     src: 'static/trophy_silver.png',
                //     width: 100,
                //     height: 100
                //     },
                // ]
            }
        },
        // layout: {
        //     padding: {
        //     top: 100
        //     }
        // },
        legend: {
            display: false
        },
        scales: {
            scaleShowLabels: true,
            xAxes: [{
                gridLines: {
                    display: false,
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
                    display: false,
                },
                ticks: {
                    display: false,
                },
                grid: {
                    display: false
                }
            }]
        }
    }
});