from flask import Flask, render_template, request

app = Flask(__name__)

"""
@app.route('/')
def principal():
    return "Bienvenido al sitio web de Aaron / Suscribete"

@app.route('/contacto')
def contacto():
    return "Aquí podemos ponernos en contacto"
"""
@app.route('/') 
def principal():
    return render_template('index.html')


@app.route('/lenguajes')
def mostrarLenguajes():
    misLenguajes = ("Fortnite", "Halo", "Minecraft", "Terraria",
                    "Left 4 dead 2", "Geometry Dash", "Age Of Empire ll", "Apex Legends")
    return render_template('lenguajes.html', lenguajes=misLenguajes)


@app.route('/contacto' , methods = ['GET','POST'])
def contacto():
    user = {
        'name': '',
        'email':''
    }
    if request.args:
        user['name'] = request.args['nombre']
        user['email'] = request.args['correo']
        
    if request.method == 'POST':
        user['name'] = request.form['nombre']
        user['email'] = request.form['correo']
        
    return render_template('contacto.html', usuario=user)


if __name__ == '__main__':
    app.run(debug=True)