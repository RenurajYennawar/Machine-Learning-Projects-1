from flask import Flask, render_template,request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

#class = { 0:'Not eligible',1:'eligible'}

@app.route('/')

def home():
    return render_template('basic.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_list =[]
    for i in request.form.values():
        try:
            input_list.append(int(i))
        except:
            input_list.append(float(i))
    final_features = np.array(input_list)
    #print(final_features)
    prediction = model.predict([final_features])
    print(prediction)
    output = prediction[0]

    return render_template('basic.html',predicted_output='Petrol consumption is {}'.format(output))


if __name__ == '__main__':
    app.run(debug=True)