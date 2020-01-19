var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',
    // The data for our dataset
    data: {
        labels: ['00', '05', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55'],
        datasets: [{
            label: 'Ontario Energy Demand',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: consumption
        }]
    },
    // Configuration options go here
    options: {}
});
