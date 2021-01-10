from flask import Flask, jsonify, request
import json

app = Flask(__name__)


#Datos hardcode
algo = [
    {
        "nombre" : "nombre1",
        "valor" : "valor1"
    },
    {
        "nombre" : "nombre2",
        "valor" : "valor2"
    },
    {
        "nombre" : "nombre3",
        "valor" : "valor3"
    }
]


#Metodo GET del API algo
@app.route('/algo', methods=['GET'])
@app.route('/algo/<name>', methods=['GET'])
def optenerAlgo(name = None):
    if name == None:
        return jsonify(algo), 200
    else:
        nombre = next((elem for elem in algo if elem['nombre'] == name), None)
    
    if nombre == None:
        return "Algo not found", 404
    else:
        return jsonify(nombre), 200


#Metodo POST del API algo
@app.route('/algo', methods=['POST'])
def insertarAlgo():
    data = json.loads(request.data)
    
    nombre = data["nombre"]
    valor = data["valor"]

    newAlgo = {
        "nombre" : nombre,
        "valor" : valor
    }

    algo.append(newAlgo)

    return jsonify(newAlgo), 200


#Metodo DELETE del API algo
@app.route('/algo', methods=['DELETE'])
def eliminarAlgo():
    return None


#Metodo PUT del API algo
@app.route('/algo', methods=['PUT'])
def actualizarAlgo():
    return None



if __name__ == "__main__":
    app.run(debug=True)