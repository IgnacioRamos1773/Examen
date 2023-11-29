from flask import Flask, render_template, request, session

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Ejercicio1', methods=['GET','POST'])
def Ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        total = tarros * 9000

        if edad >= 18 and edad <= 30:
            dscto = total*15/100

        elif edad > 30:
            dscto = total*25/100

        else:
            dscto = 0

        pagar = total - dscto

        return render_template('Formulario.html',nombre=nombre, total=total, dscto=dscto, pagar=pagar)
    return render_template('Formulario.html')


app.config['SECRET_KEY'] = 'ignacio'

usuarios = {
    "juan": "admin",
    "pepe": "user"
}

@app.route('/Ejercicio2', methods=['GET', 'POST'])
def Ejercicio2():
    mensaje = ''
    user = ''
    contrasena = ''

    if request.method == 'POST':
        user = request.form['user']
        contrasena = request.form['contrasena']

        if user in usuarios and usuarios[user] == contrasena:
            session['usuario'] = user

            if user == 'juan':
                mensaje = 'Bienvenido administrador Juan'
            elif user == 'pepe':
                mensaje = 'Bienvenido usuario Pepe'
            else:
                mensaje = 'Usuario o contraseña incorrectos'
        else:
            mensaje = 'Usuario o contraseña incorrectos'

    return render_template('Formulario2.html', user=user, contrasena=contrasena, mensaje=mensaje)

if __name__ == '__main__':
    app.run()
