from flask import Flask, request, jsonify

app = Flask(__name__)

# Este dicionário vai armazenar os dados enviados via POST
dados_armazenados = {}

@app.route('/producao', methods=['GET','POST'])
def producao_methods():
    if request.method == 'POST':
        global dados_armazenados
        # Obtém os dados JSON enviados na requisição
        dados_json = request.get_json()
        # Armazena os dados
        dados_armazenados = dados_json
        # Retorna uma resposta
        return jsonify({'mensagem': 'Dados enviados com sucesso!'}), 200
    else:
        return jsonify(dados_armazenados), 200

@app.route('/processamento', methods=['GET','POST'])
def processamento_methods():
    if request.method == 'POST':
        global dados_armazenados
        # Obtém os dados JSON enviados na requisição
        dados_json = request.get_json()
        # Armazena os dados
        dados_armazenados = dados_json
        # Retorna uma resposta
        return jsonify({'mensagem': 'Dados enviados com sucesso!'}), 200
    else:
        return jsonify(dados_armazenados), 200

@app.route('/comercializacao', methods=['GET','POST'])
def comercializacao_methods():
    if request.method == 'POST':
        global dados_armazenados
        # Obtém os dados JSON enviados na requisição
        dados_json = request.get_json()
        # Armazena os dados
        dados_armazenados = dados_json
        # Retorna uma resposta
        return jsonify({'mensagem': 'Dados enviados com sucesso!'}), 200
    else:
        return jsonify(dados_armazenados), 200
    
@app.route('/importacao', methods=['GET','POST'])
def importacao_methods():
    if request.method == 'POST':
        global dados_armazenados
        # Obtém os dados JSON enviados na requisição
        dados_json = request.get_json()
        # Armazena os dados
        dados_armazenados = dados_json
        # Retorna uma resposta
        return jsonify({'mensagem': 'Dados enviados com sucesso!'}), 200
    else:
        return jsonify(dados_armazenados), 200
    

@app.route('/exportacao', methods=['GET','POST'])
def exportacao_methods():
    if request.method == 'POST':
        global dados_armazenados
        # Obtém os dados JSON enviados na requisição
        dados_json = request.get_json()
        # Armazena os dados
        dados_armazenados = dados_json
        # Retorna uma resposta
        return jsonify({'mensagem': 'Dados enviados com sucesso!'}), 200
    else:
        return jsonify(dados_armazenados), 200
    

@app.route('/publicacao', methods=['GET','POST'])
def publicacao_methods():
    if request.method == 'POST':
        global dados_armazenados
        # Obtém os dados JSON enviados na requisição
        dados_json = request.get_json()
        # Armazena os dados
        dados_armazenados = dados_json
        # Retorna uma resposta
        return jsonify({'mensagem': 'Dados enviados com sucesso!'}), 200
    else:
        return jsonify(dados_armazenados), 200