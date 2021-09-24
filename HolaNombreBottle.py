from bottle import Bottle, run, template, request, redirect

app = Bottle()

@app.route('/')
@app.route('/hola/<name>') # Ruta dinámica
def hello(name = 'Extraño'):
    return template('Hola {{name}}, cómo estás?', name = name)

@app.route('/loged/<name>')
def loged(name = 'Extraño'):
    return template('''You're in! {{name}}''', name = name)

# Método de login básico
def checkLogin(username, password):
    isLogged = False
    if username == 'max' and password == '123':
        isLogged = True
    return isLogged

# Ruta que muestra el formulario del login
@app.route('/login', method = 'GET') # GET: traer información
def login():
    isFailed = '0' if request.query.Failed == '' else request.query.Failed

    # Genera contenido de web dinámico que se va a presentar
    # POST: envía información
    formString = '''<form action="/login" method="post">
            Username: <input name="username" type="text"/>
            Password: <input name="password" type="password"/>
            <input value="Login" type="submit"/>
        </form>
    '''

    if int(isFailed) == 1:
        return '<p><strong>Login failed!</p>' + formString
    else:
        return formString

# No se deben tener más de dos rutas iguales con diferentes métodos
# en este caso se tienen dos métodos con la misma ruta, así que dependiendo
# de dicho método, se toma la parte que lo llama
@app.post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if checkLogin(username, password):
        redirect(f"/loged/{username}")
    else:
        redirect("/login?Failed=1") # Párametros verificados en URL

run(app, host = 'localhost', port = 3333, debug = True)