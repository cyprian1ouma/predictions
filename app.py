from flask import Flask, jsonify # type: ignore
import random

app = Flask(__name__)

# Define percentage weights for numbers 0-9
weights = [0.07, 0.09, 0.11, 0.13, 0.09, 0.08, 0.07, 0.08, 0.09, 0.09]
def home():
    return render_template('index.html') # type: ignore


@app.route('/predict', methods=['GET'])
def predict():
    # Normalize weights to sum to 1
    total_weight = sum(weights)
    normalized_weights = [weight / total_weight for weight in weights]

    # Generate a predicted number based on weights
    predicted_number = random.choices(range(10), weights=normalized_weights, k=1)[0]
    
    return jsonify(predicted_number=predicted_number)

if __name__ == '__main__':
    app.run(debug=True)
