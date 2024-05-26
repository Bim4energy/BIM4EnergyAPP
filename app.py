import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    case_select = data['caseSelect']
    climate_select = data['climateSelect']
    windows_u_value = data['windowsUValue']
    heating_system = data['heatingSystem']

    # Dummy calculation for energy consumption
    base_heating = 100  # Example base case value
    improved_heating = base_heating * (1 - (windows_u_value + heating_system) / 10)
    base_cooling = 50   # Example base case value
    improved_cooling = base_cooling * (1 - (windows_u_value + heating_system) / 20)

    response = {
        'heating': [base_heating, improved_heating],
        'cooling': [base_cooling, improved_cooling],
    }
    
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
