from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import pickle
import librosa
import numpy as np


load_model = pickle.load(open('phase1_model.sav','rb'))
load_model2 = pickle.load(open('phase2_model.sav', 'rb')) 


def check(file):
    result = load_model.predict(tetsting_unit(file))
    if result[0] == 2:  # checking sound noise or human
            ok = load_model2.predict(tetsting_unit(file))  # using second phase_model
            if ok[0] == 1:
                # print("Phase-2 clear")
                return('Scream')
                # print(True)
            else:
                return('speech')
                # print(False)
    else:
            # print("noise")
            return("Noise")

def tetsting_unit(filename):
    tester = []
    test, ans = librosa.load(filename)  # provide path of  wave file
    mfccs = np.mean(librosa.feature.mfcc(y = test, sr = ans, n_mfcc=40).T, axis=0)
    tester.append(mfccs)
    tester = np.array(tester)
    return tester 

app = Flask(__name__)

# Specify the allowed file extensions
ALLOWED_EXTENSIONS = {'wav'}

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# API endpoint for file upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Check if the request contains a file
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']

    # Check if the file is allowed
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = './dumps/' 
        file.save(file_path + filename)

        # Call the ML model function with the file path
        prediction = check(file_path + filename)

        # Return the prediction as the API response
        return jsonify({'prediction': prediction})

    return jsonify({'error': 'Invalid file format'})

if __name__ == '__main__':
    app.run()
