from flask import Flask, request, jsonify
import diabetes_prediction_app

app = Flask(__name__)

@app.route('/predict_diabetes', methods=['POST'])
def predict_diabetes_api():
    try:
        data = request.get_json()
        if all(key in data for key in ['pregnancies', 'glucose', 'blood_pressure', 'skin_thickness', 'insulin', 'bmi', 'diabetes_pedigree', 'age']):
            pregnancies = data['pregnancies']
            glucose = data['glucose']
            blood_pressure = data['blood_pressure']
            skin_thickness = data['skin_thickness']
            insulin = data['insulin']
            bmi = data['bmi']
            diabetes_pedigree = data['diabetes_pedigree']
            age = data['age']

            result = diabetes_prediction_app.predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age)
            return jsonify({'prediction': result})
        else:
            return jsonify({'error': 'Missing parameters'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
