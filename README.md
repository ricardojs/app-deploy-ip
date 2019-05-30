# API Deploy

## Requisitos
* Python
* Flask
* peewee
* jsonify
* request
* docker-compose

## Teste da aplicação

Para testar usei o **docker-compose**.
Também podendo ser usando na AWS [Amazon ECS CLI Tutorial](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI_tutorial.html)

Basta instalar o docker-compose no Ubuntu:
```
sudo apt-get install docker-compose
```
Executar o docker-compose:
```
docker-compose up -d
```

## Usando a API de Deploy

### GET
Retornar uma lista de itens na lista de deploys:
```
curl http://localhost:5000/deploys
```

Obtenha todas as informações disponíveis para um item específico:
```
curl http://localhost:5000/deploys/1
```

### POST
Crie um novo item de deploy, O corpo POST é um objeto JSON conforme o exemplo abaixo:
```
curl -H "Content-Type: application/json" -X POST -d '{"componente":"Componente1","versao":"2.0","responsavel":"Ricardo","status":"to-do"}' http://localhost:5000/deploys
```

### PUT
Modifique uma deploy existente, subistituindo o id e os campos que deseja alterar.
```
curl -X PUT -H "Content-Type: application/json" -d '{"componente":"Abacate","versao":"2.0","responsavel":"Mario","status":"Done" }' http://localhost:5000/deploys/id
```

### DELETE
Remover um  deploys, subistituindo id pelo numero do deploy que deseja remover.
```
curl -X DELETE http://localhost:5000/deploys/id
```
