from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__, template_folder='App/templates', static_folder='App/static')

# Load the trained model and preprocessor
try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, 'App/models/dtr.pkl')
    preprocessor_path = os.path.join(base_dir, 'App/models/preprocessor.pkl')

    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    
    with open(preprocessor_path, 'rb') as preprocessor_file:
        preprocessor = pickle.load(preprocessor_file)
    
    print("Models loaded successfully!")
except Exception as e:
    print(f"Error loading models: {e}")

# Global variables for UI dropdowns
crops = ["Paddy", "Wheat", "Barley", "Maize", "Pearl Millet", "Finger Millet",
         "Indian Mustard", "Groundnut", "Bengal Gram", "Sugarcane", "Jute", "Mesta", "Cotton"]
states = ["Andhra Pradesh", "Tamil Nadu", "Gujarat", "Orissa", "West Bengal", 
          "Himachal Pradesh", "Uttarakhand", "Jammu And Kashmir", "Arunachal Pradesh", 
          "Assam", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Sikkim", "Tripura",
          "Chhattisgarh", "Madhya Pradesh", "Bihar", "Uttar Pradesh", "Rajasthan", 
          "Maharashtra", "Karnataka", "Punjab", "Haryana", "Delhi", "Jharkhand", "Kerala"]
varieties = {
    "Paddy": ["Chinsurah Rice (IET 19140)", "(CNI 383-5-11)", "IGKVR-1 (IET 19569)", "IGKVR-2 (IET 19795)",
              "CR Dhan 401 (REETA)", "CR Dhan 601 (IET 18558)", "CR Dhan 501 (IET 19189)", 
              "RC Maniphou 11 (IET 20193)"],
    "Wheat": ["MPO(JW) 1215 (MPO 1215)", "MACS 6222", "PDW 314", "DBW39", 
              "VL Gehun 907 (VL 907)", "Pusa Suketi HS 507", "Pusa Prachi (HI 1563)", 
              "WHD 943", "Netravati (NIAW 1415)"],
    "Barley": ["BH-902", "DWRB 73", "Pusa Losar (BH-380)"],
    "Maize": ["HSC1", "HQPM-4", "MCH 36 (Hybrid) (DKC 9099)", "DHM 119 (BH 4062)", 
              "PMH 4 (JH 31153)", "PMH 5 (JH 3110)"]
}
units = ['Quintals', 'Tons']

state_crop_variety_map = {
    "Andhra Pradesh": {
        "Paddy": ["Chinsurah Rice (IET 19140)", "CR Dhan 401 (REETA)", "CR Dhan 601 (IET 18558)"],
        "Groundnut": ["Kadiri Harithandhra (K 1319)", "GPBD 5"]
    },
    "Nagaland": {
        "Paddy": ["(CNI 383-5-11)"],
        "Wheat": ["Pusa Suketi HS 507", "Pusa Prachi (HI 1563)"]
    },
    "Tamil Nadu": {
        "Paddy": ["Chinsurah Rice (IET 19140)"]
    },
    "Gujarat": {
        "Paddy": ["Chinsurah Rice (IET 19140)"]
    },
    "Orissa": {
        "Paddy": ["Chinsurah Rice (IET 19140)"]
    },
    "West Bengal": {
        "Paddy": ["Chinsurah Rice (IET 19140)"]
    }
}

@app.route('/')
def index():
    try:
        return render_template('index.html', crops=crops, states=states, varieties=varieties, units=units)
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form data
        crop = request.form.get('crop')
        variety = request.form.get('variety')
        state = request.form.get('state')
        cost = float(request.form.get('cost'))
        quantity = float(request.form.get('quantity'))
        duration = int(request.form.get('duration'))
        unit = request.form.get('unit')

        # Debugging input values
        print(f"Inputs: Crop={crop}, Variety={variety}, State={state}, Cost={cost}, Quantity={quantity}, Duration={duration}")

        # Preprocess and predict
        input_features = [crop, variety, state, cost, quantity, duration]

        try:
            input_features_transformed = preprocessor.transform([input_features])
            prediction = model.predict(input_features_transformed)
            if unit == 'Tons':
                prediction = prediction * 10  # Assuming 1 ton = 10 quintals

            return render_template('index.html', prediction=prediction, unit=unit, 
                                   crops=crops, states=states, varieties=varieties, units=units)
        except ValueError as e:
            # Handle unknown categories
            state_info = state_crop_variety_map.get(state, {})
            available_crops_varieties = {crop: state_info.get(crop, []) for crop in state_info}
            recommended_states = [s for s in state_crop_variety_map if variety in state_crop_variety_map[s].get(crop, [])]

            error_message = f"An error occurred: {e}. Based on the state '{state}', here are the available crops and their varieties:"
            return render_template('index.html', error_message=error_message, state=state, crop=crop, 
                                   variety=variety, available_crops_varieties=available_crops_varieties, 
                                   recommended_states=recommended_states, crops=crops, states=states, 
                                   varieties=varieties, units=units)
    except Exception as e:
        # Debugging: Print error message
        print(f"Error during prediction: {e}")
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run()
