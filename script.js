document.getElementById("predict-btn").addEventListener("click", function() {
    fetch('/predict')
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = `Predicted Number: ${data.predicted_number}`;
        })
        .catch(error => console.error('Error:', error));
});
