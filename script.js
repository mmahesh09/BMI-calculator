document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const resultContainer = document.getElementById('results');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const weight = parseFloat(document.querySelector('#weight').value);
        const heightFeet = parseInt(document.querySelector('#heightFeet').value);
        const heightInches = parseInt(document.querySelector('#heightInches').value);

        const response = await fetch('/api/calculate_bmi', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ weight, heightFeet, heightInches })
        });
        const data = await response.json();

        resultContainer.innerHTML = `
            <p id="bmiResult">Your BMI is: ${data.bmi}</p>
            <p id="bmiCategory">You are categorized as: ${data.bmiCategory}</p>
            <p id="advice">Advice: ${data.advice}</p>
        `;
    });
});
