import requests

url = 'http://localhost:8080/people/post'
data = {
    'nombre': 'Pepino',
    'apellido': 'pepote',
    'correo': 'pepo@pepo.es',
    'edad': 50
}

response = requests.post(url, json=data)
if response.status_code == 200:
    print('Miembro insertado correctamente')
else:
    print('Error al insertar miembro')