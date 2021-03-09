from flask import Flask, render_template, request
from chat_code import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/chatbot")
def index():
    return render_template('index_cb.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery1.html')
  


@app.route("/get")
def chat():
    userText = request.args.get('msg')
    
    while True:

            results = model.predict([bag_of_words(userText, words)])
            results_index = numpy.argmax(results)
            tag = labels[results_index]
            if userText.lower()=="bye":
                responce="Oh okay bye! Had a nice time chatting with you"
                return (responce)
                break;
            
            for tg in data["COVID-19"]:
                if tg['tag'] == tag:
                    responses = tg['responses']

            responce= random.choice(responses)
            return responce
        

if __name__ == "__main__":
    app.run()