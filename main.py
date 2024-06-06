from flask import Flask, render_template, request, redirect
app = Flask(__name__)

consultas = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/serviço')
def serviço():
    return render_template('serviço.html')

@app.route('/agendamento', methods=['GET', 'POST'])
def agendamento():
    if request.method == 'POST':
        nome_animal = request.form['nome_animal']
        nome_tutor = request.form['nome_tutor']
        data = request.form['data']
        horario = request.form['horario']
        codigo = len(consultas)
        consultas.append([codigo, nome_animal, nome_tutor, data, horario,])
        return redirect('/')
    else:
        return render_template('agendamento.html')

if __name__ == '__main__':
    app.run(debug=True)