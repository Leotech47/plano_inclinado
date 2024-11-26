from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_forcas(massa, angulo, coeficiente_atrito=0):
    # ... (mesmo código Python que você já tem)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # ... (processamento dos dados do formulário)
        return render_template('resultado.html', forcas=forcas)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
  
