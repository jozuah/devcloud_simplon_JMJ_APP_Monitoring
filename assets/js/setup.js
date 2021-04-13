async function fetch_data_api() {
    let url = 'http://jmjappmonitoring-back.azurewebsites.net/api/?cost=AllTimeBySubscriptionName';
    
    try {
        let res = await fetch(url)
        let datas = await res.json()
        const cost = [];
        const labels = []

        datas.forEach(data => {
            cost.push(data['CoutTotal'])
            labels.push(data['SubscriptionName'])
        })

        const option = {
            responsive: false,
            scales: {
                yAxes: [{
                stacked: false,
                gridLines: {
                    display: true,
                    color: "rgba(255,99,132,0.2)"
                    }
                }],
                xAxes: [{
                    ticks: {
                        autoSkip: false
                    },
                gridLines: {
                    display: false
                    }
                }]
            },
            tooltips: {
                cornerRadius: 0,
                caretSize: 0,
                xPadding: 16,
                yPadding: 10,
                backgroundColor: 'crimson',
                titleFontStyle: 'normal',
                titleMarginBottom: 15
                }
            };

            const dataChart = {
                labels: labels,
                datasets: [{
                    label: 'All Costs for SubcriptionName',
                    data: cost,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 205, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(201, 203, 207, 0.2)',
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 205, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(54, 162, 235, 0.2)'
                    ],
                    borderColor: [
                        'rgb(255, 99, 132)',
                        'rgb(255, 159, 64)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
                        'rgb(54, 162, 235)',
                        'rgb(153, 102, 255)',
                        'rgb(201, 203, 207)',
                        'rgb(255, 99, 132)',
                        'rgb(255, 159, 64)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
                        'rgb(54, 162, 235)'
                    ],
                    borderWidth: 1
                }]
            };

            const config = {
                type: 'bar',
                data: dataChart,
                options: option
            };

            const myChart = new Chart(document.getElementById('barChart'), config);

    } catch(error) {
        console.log(error);
    }
}


fetch_data_api()
