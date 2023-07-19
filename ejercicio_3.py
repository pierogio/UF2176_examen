"""3)	Genera una pequeña aplicación, para registrar un usuario en memoria o base de datos. Tendrás que tener una clase en un fichero repository, donde haya diferentes métodos (add, get … ).
La aplicación tendrá dos puntos de entrada:
-	“/create/user”  Creación de usuario
                       Ejemplo: POST  /créate/user/1/pepe/25
-	“/user/id”  Obtención de usuario
                       Ejemplo: GET  /user/1
            Cuando llamamos al endpoint de creación de usuario, se tendrá que añadir en memoria el usuario o conectar con base de datos y hacer el respectivo INSERT, en la correspondiente tabla.
Cuando llamamos al endpoint de obtención de usuario, el repositorio tendrá que devolvernos el usuario añadido anteriormente.
Los atributos del usuario pueden ser: id, name, age .. (opcional)
En caso de que no puedas implementar la capa de red, puedes hacer solo la capa de repositorio y su ejecución añadiendo los datos manualmente como hemos hecho en ejercicios de clase (puntuará menos)."""

from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)


def connection_database():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        port=int(3307),
        database='people'
    )
    return connection


def execute_query(query, connection):
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

@app.route('/people/<int:miembro_id>', methods=['GET'])
def get_miembro(miembro_id):
    connection = connection_database()
    query = f"SELECT * FROM miembros WHERE id = {miembro_id}"
    result = execute_query(query, connection)
    connection.close()
    return str(result)


@app.route('/people/post', methods=['POST'])
def post_miembros():
    try:
        connection = connection_database()
        query = "INSERT INTO miembros (nombre, apellido, correo, edad) VALUES (%s, %s, %s, %s)"
        values = (request.json['nombre'], request.json['apellido'], request.json['correo'], request.json['edad'])
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        connection.close()
        return jsonify({'mensaje': 'miembro insertado correctamente'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
 
