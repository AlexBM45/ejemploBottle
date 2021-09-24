from bottle import Bottle, run

'''
BOOTLE: microframework básico de Python que permite desarrollo web,
microservicios y ApiREST
'''

# APLICACIÓN MONOLÍTICA: maneja front y back al mismo tiempo
app = Bottle()

@app.route('/')
@app.route('/hola')
# ambas rutas responden a la función
def hello():
    return 'Hola Mundo!'

run(app, host = 'localhost', port = 8080, debug = True)