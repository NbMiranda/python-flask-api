from flask import Flask, make_response, jsonify, request
import mysql.connector

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

mydb = mysql.connector.connect(host='172.17.0.2', user='root', password='password', database='python')
cursor = mydb.cursor()

# CREATE
@app.route("/carros", methods=['POST'])
def createCarro():
    carro = request.json

    sql = f"INSERT INTO carros (marca, modelo, ano) VALUES ('{carro['marca']}', '{carro['modelo']}', {carro['ano']})"
    cursor.execute(sql)
    mydb.commit()

    return make_response(
        jsonify(
            mensagem='Carro cadastrado com sucesso: ',
            dados=carro
        )
    )

# READ
@app.route("/carros", methods=['GET'])
def getCarros():

    cursor.execute('SELECT * FROM carros')
    myCars = cursor.fetchall()

    return make_response(
        jsonify(
            mensagem='Lista de carros: ',
            dados=myCars
        )
    )

# READ ONE
@app.route("/carros/<int:id>", methods=['GET'])
def getCarById(id):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM carros WHERE id = %s", (id,))
    carro = cursor.fetchone()

    if carro:
        return carro

    return None

#UPDATE
#UPDATE
@app.route("/carros/<int:id>", methods=['PUT'])
def updateCarRoute(id):
    data = request.json

    if 'modelo' in data:
        modelo = data['modelo']
        # Faça a atualização do campo 'modelo' no banco de dados
        updateCar(id, {'modelo': modelo})

    if 'marca' in data:
        marca = data['marca']
        # Faça a atualização do campo 'marca' no banco de dados
        updateCar(id, {'marca': marca})

    if 'ano' in data:
        ano = data['ano']
        # Faça a atualização do campo 'ano' no banco de dados
        updateCar(id, {'ano': ano})

    updatedCar = getCarById(id)

    if updatedCar:
        return make_response(
            jsonify(
                message="Carro atualizado",
                data=updatedCar
            )
        )
    else:
        return make_response(
            jsonify(
                message="Nenhum campo atualizado.",
                data=None
            )
        )


def updateCar(id, data):
    column = next(iter(data))
    value = data[column]

    sql = f"UPDATE carros SET {column} = '{value}' WHERE id = {id}"
    cursor.execute(sql)
    mydb.commit()


# DELETE
@app.route("/carros/<int:id>", methods=['DELETE'])
def deleteCarro(id):
    carro = getCarById(id)

    if carro is None:
        return "Carro não encontrado", 404

    cursor = mydb.cursor()
    sql = "DELETE FROM carros WHERE id = %s"
    cursor.execute(sql, (id,))
    mydb.commit()

    return "Carro deletado com sucesso!", 200


@app.route("/")
def hello():
    return "Olá seja bem vindo ao meu simples CRUD de carros!"


if __name__ == "__main__":
    app.run(debug=True)
