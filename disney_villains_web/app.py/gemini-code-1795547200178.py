from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', active_page='inicio')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html', active_page='nosotros')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', active_page='servicios')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    mensaje_enviado = False
    datos_usuario = {}
    
    if request.method == 'POST':
        datos_usuario = {
            'nombre': request.form.get('nombre'),
            'email': request.form.get('email'),
            'asunto': request.form.get('asunto'),
            'mensaje': request.form.get('mensaje')
        }
        mensaje_enviado = True
        
    return render_template(
        'contacto.html', 
        active_page='contacto', 
        mensaje_enviado=mensaje_enviado, 
        datos=datos_usuario
    )

if __name__ == '__main__':
    app.run(debug=True)