from flask import Flask,render_template,request, jsonify
import pickle
model = pickle.load(open('model.pickle','rb'))
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "exp://192.168.133.249:8081"}})

# @app.route('/')
# def home():
#     result=''
#     return render_template('index.html',**locals())

# @app.route('/api/data',methods=['GET'])
# def get_data():
#     prices = float(request.form['price'])
#     result = model.predict([[prices]])[0]
#     return render_template('index.html',**locals())


# @app.route('/predict',methods=['POST','GET'])
# def predict():
#     prices = float(request.form['price'])
#     result = model.predict([[prices]])[0]
#     return render_template('index.html',**locals())

with open('model.pickle', 'rb') as f:
    model = pickle.load(f)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    area = data['area']
    prediction = model.predict([[area]])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)