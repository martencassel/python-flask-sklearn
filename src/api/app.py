from flask import Flask
import pickle
import json

X_test=[[6,148,72,35,0,33.6,0.627,50]]
Y_test=[[1]]

model = pickle.load(open("models/finalized_model.sav", "rb"))

app = Flask(__name__)

@app.route('/health')
def health_check():
    return 'backend is running'

@app.route('/predict')
def predict():
    print(model)
    result = model.score(X_test, Y_test)
    print(result)
    return json.dumps(result)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8093)
