from flask import Flask, render_template, request, redirect
app = Flask(__name__)

consultas = []

pacientes = []

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

@app.route('/')
def index():
    return render_template('index.html', pacientes=pacientes)

@app.route('/inserir_paciente', methods=['GET', 'POST'])
def inserir_paciente():
    """
    Rota para adicionar um novo contato.
    Se o método for POST, adiciona o novo contato à lista.
    Se não, exibe o formulário para adicionar um novo contato.
    """
    if request.method == 'POST':
        nome = request.form['nome']
        raca = request.form['raca']
        especie = request.form['especie']
        peso = request.form['peso']
        nome_tutor1 = request.form['nome_tutor1']
        telefone = request.form['telefone']
        codigo = len(pacientes)
        pacientes.append([codigo, nome, telefone, raca, peso, especie, nome_tutor1])
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        return render_template('inserir_paciente.html')  # Renderiza o formulário de adicionar contato


@app.route('/editar_paciente/<int:codigo>', methods=['GET', 'POST'])
def editar_paciente(codigo):
    """
    Rota para editar um contato existente.
    Se o método for POST, atualiza os detalhes do contato com o ID fornecido.
    Caso contrário, exibe o formulário preenchido com os detalhes do contato para edição.
    """
    if nome = request.form['nome']
    raca = request.form['raca']
    especie = request.form['especie']
    peso = request.form['peso']
    nome_tutor1 = request.form['nome_tutor1']
    telefone = request.form['telefone']
    codigo = len(pacientes)
    pacientes.append([codigo, nome, telefone, raca, peso, especie, nome_tutor1])
    return redirect('/')  # Redireciona de volta para a página inicial

else:
contato = pacientes[codigo]
return render_template('editar_paciente.html', contato=contato)  # Renderiza o formulário de edição


@app.route('/idadehumana', methods=['GET', 'POST'])
def idadehumana():


if request.method == 'POST':
    especie2 = request.form['especie2']
    idade2 = int(request.form['idade2'])

    if especie2.lower() == 'cachorro':
        if idade2 == 1:
            idade_humana = 15
        elif idade2 == 2:
            idade_humana = 24
        elif idade2 == 3:
            idade_humana = 28
        elif idade2 == 4:
            idade_humana = 32
        elif idade2 == 5:
            idade_humana = 36
        elif idade2 == 6:
            idade_humana = 40
        elif idade2 == 7:
            idade_humana = 44
        else:
            idade_humana = 44 + (idade2 - 7) * 5

    elif especie2.lower() == 'gato':
        if idade2 == 1:
            idade_humana = 15
        elif idade2 == 2:
            idade_humana = 24
        elif idade2 == 3:
            idade_humana = 28
        elif idade2 == 4:
            idade_humana = 32
        elif idade2 == 5:
            idade_humana = 36
        else:
            idade_humana = 36 + (idade2 - 5) * 4

    return render_template('idade_humana.html', idade_humana=idade_humana)
else:
    return render_template('idadehumana.html')


@app.route('/medicamento_mg', methods=['GET', 'POST'])
def medicamento_mg():
    if request.method == 'POST':
        peso = request.form['peso']
        doseremedio = int(request.form['doseremedio'])
        medicamento_mg = (peso * doseremedio)
        return render_template('medicamento_mg.html', medicamento_mg=medicamento_mg)

@app.route('/')
def quantidade_mililitros_soro.html():
return render_template('quantidade_mililitros_soro.html')


@app.route('/quantidade_mililitros_soro/', methods=['POST'])
def verificar_quantidade_mililitros_soro():

peso_animal = float(request.form['peso_animal'])
grau_desidatracao = request.form['grau_desidatracao']
if grau_desidatracao.lower() == 'leve':
volume_fluidoterapia = 50 * peso_animal
elif grau_desidatracao.lower() == 'moderada':
volume_fluidoterapia = 75 * peso_animal
elif grau_desidatracao.lower() == 'grave':
volume_fluidoterapia = 100 * peso_animal

return render_template('quantidade_mililitros_soro.html')
if __name__ == '__main__':
    app.run(debug=True)