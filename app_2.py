from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', hasil_prediksi_tanaman="")

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    nitrogen, fosfor, kalium, suhu, kelembaban, phtanah, curahhujan  = [x for x in request.form.values()]

    data = []

    data.append(float(nitrogen))
    data.append(float(fosfor))
    data.append(float(kalium))
    data.append(float(suhu))
    data.append(float(kelembaban))
    data.append(float(phtanah))
    data.append(float(curahhujan))
    # if sex == 'Laki-laki':
    #     data.extend([0, 1])
    # else:
    #     data.extend([1, 0])

    # if smoker == 'Ya':
    #     data.extend([0, 1])
    # else:
    #     data.extend([1, 0])
    
    nama = {0 : 'rice', 1 : 'maize', 2 : 'chickpea', 3 : 'kidneybeans', 4 : 'pigeonpeas',
       5 : 'mothbeans', 6 : 'mungbean', 7 : 'blackgram', 8 : 'lentil', 9 : 'pomegranate',
       10 : 'banana', 11 : 'mango', 12 : 'grapes', 13 : 'watermelon', 14 : 'muskmelon', 15 : 'apple',
       16 : 'orange', 17 : 'papaya', 18 : 'coconut', 19 : 'cotton', 20 : 'jute', 21 : 'coffee'}

    prediction = model.predict([data])
    output = nama[prediction[0]]

    return render_template('index.html', hasil_prediksi_tanaman=output, nitrogen=nitrogen, fosfor=fosfor, kalium=kalium, suhu=suhu, kelembaban=kelembaban, phtanah=phtanah, curahhujan=curahhujan)


if __name__ == '__main__':
    app.run(debug=True)