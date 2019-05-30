# -*- coding: utf-8 -*-
import peewee
import datetime
from flask import Flask, jsonify, request

banco = peewee.SqliteDatabase('banco.db')

class Deploy(peewee.Model):
    componente = peewee.TextField()
    versao = peewee.FloatField()
    responsavel = peewee.TextField()
    status = peewee.TextField()
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)

    def to_dict(self):
        return {'id':self.id, 'componente': self.componente, 'versao': self.versao, 'responsavel': self.responsavel, 'status': self.status, 'timestamp': self.timestamp}

    class Meta:
        database = banco
try:
    banco.create_table(Deploy)
except Exception as e:
    pass

app = Flask(__name__)

# INDEX
@app.route("/")
def index():
    return "Bem Vindo a API Time Deploy"

# GET /deploys/
@app.route('/deploys')
def deploys():
    return jsonify([deploy.to_dict() for deploy in Deploy.select()])

# PUT/PATCH /deploys/id
@app.route('/deploys/<int:id_deploy>', methods=['PUT', 'PATCH'])
def editar_deploy(id_deploy):
    dados = request.json

    try:
        deploy = Deploy.get(id=id_deploy)
    except Deploy.DoesNotExist as e:
        return jsonify({'status': 404, 'mensagem': 'Deploy nao encontrada'}), 404

    deploy.componente = dados['componente']
    deploy.versao = dados['versao']
    deploy.responsavel = dados['responsavel']
    deploy.status = dados['status']
    deploy.save()

    return jsonify({'status': 200, 'mensagem': 'Deploy salvo com sucesso'})

# DELETE /deploys/id
@app.route('/deploys/<int:id_deploy>', methods=['DELETE'])
def apagar_deploy(id_deploy):
    try:
        deploy = Deploy.get(id=id_deploy)
        deploy.delete_instance()

        return jsonify({'status': 200, 'mensagem': 'Deploy excluido com sucesso'})

    except Deploy.DoesNotExist:
        return jsonify({'status': 404, 'mensagem': 'Deploy nao encontrado'})

# GET /deploys/id
@app.route('/deploys/<int:id_deploy>')
def deploy(id_deploy):
    try:
        deploy = Deploy.get(id=id_deploy)
        return jsonify(deploy.to_dict())
    except Deploy.DoesNotExist:
        return jsonify({'status': 404, 'mensagem': 'Deploy nao encontrado'})

# POST /deploys/
@app.route('/deploys', methods=['POST'])
def nova_deploy():
    dados = request.json
    deploy = Deploy(componente=dados['componente'], versao=dados['versao'], responsavel=dados['responsavel'], status=dados['status'])
    deploy.save()

    return jsonify({'status': 200, 'mensagem': 'Deploy salvo com sucesso!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)