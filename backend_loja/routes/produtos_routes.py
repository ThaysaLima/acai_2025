from flask import Blueprint, jsonify, request
from bancodados.database import conectar_bd

produtos_bp = Blueprint("produtos", __name__)

#ROTAS:

#rota para listar produtos 
@produtos_bp.route("/", methods=["GET"])
def listar_produtos():
    conector = conectar_bd()
    cursor = conector.cursor()

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    conector.close()

    return jsonify(produtos)
#rota para obter produto específico (ID)
@produtos_bp.route("/<int:id>", methods=["GET"])
def obter_produto(id):
    conector = conectar_bd()
    cursor = conector.cursor()

    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
    produto = cursor.fetchone()

    conector.close()

    if produto:
        return jsonify(produto)
    return jsonify({"erro": "Produto não encontrado"}), 404
#rota para adicionar novo produto: 
@produtos_bp.route("/", methods=["POST"])
def adicionar_produto():
    dados = request.json

    if not dados or "nome" not in dados:
        return jsonify({"erro": "Nome do produto é obrigatório"}), 400

    conector = conectar_bd()
    cursor = conector.cursor()

    cursor.execute(
        "INSERT INTO produtos (nome, descricao, estoque_balcao, unidade_balcao, estoque_aberto, unidade_aberto, estoque_lacrado, unidade_lacrado) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (
            dados.get("nome"),
            dados.get("descricao", ""),
            dados.get("estoque_balcao", 0.0),
            dados.get("unidade_balcao", ""),
            dados.get("estoque_aberto", 0.0),
            dados.get("unidade_aberto", ""),
            dados.get("estoque_lacrado", 0.0),
            dados.get("unidade_lacrado", ""),
        ),
    )

    conector.commit()
    conector.close()

    
    return jsonify({"mensagem": "Produto adicionado com sucesso!"}), 201
