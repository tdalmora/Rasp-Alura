from flask import Flask, render_template, request
from automate import inicializaBoard, definePinoComoSaida, escreveParaPorta 

app = Flask(__name__)

inicializaBoard()
definePinoComoSaida(7)
definePinoComoSaida(11)

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def submit():
    comando=request.form['comando']
    print(comando)

    if(comando == '1ON'):
       escreveParaPorta(7,0) 
    if(comando == '1OFF'):
       escreveParaPorta(7,1)
    if(comando == '2ON'):
       escreveParaPorta(11,0)
    if(comando == '2OFF'):
       escreveParaPorta(11,1)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')