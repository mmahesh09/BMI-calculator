document.getElementById('bmi-form').addEventListener('submit', async (event) => {
    event.preventDefault();
    
    const weight = parseFloat(document.getElementById('weight').value);
    const heightFeet = parseFloat(document.getElementById('heightFeet').value);
    const heightInches = parseFloat(document.getElementById('heightInches').value);
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    // Send data to the server
    const response = await fetch('/calculate_bmi', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ weight, heightFeet, heightInches, username, password })
    });
    
    const data = await response.json();
    
    // Display results
    document.getElementById('bmiResult').innerText = `Your BMI is: ${data.bmi.toFixed(2)}`;
    document.getElementById('bmiCategory').innerText = `Category: ${data.bmiCategory}`;
    document.getElementById('advice').innerText = `Advice: ${data.advice}`;
    
    // Draw the chart
    drawChart(data.chartData);
});

function drawChart(chartData) {
    const ctx = document.getElementById('bmiChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: chartData.labels,
            datasets: [{
                label: 'BMI Progress',
                data: chartData.data,
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                fill: false
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Time'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'BMI'
                    }
                }
            }
        }
    });
}
