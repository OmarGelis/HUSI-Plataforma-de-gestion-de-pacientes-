from flask import Flask,render_template, request
from markupsafe import escape

app =  Flask(__name__)

lista_usuarios = ['Andres', 'Maria', 'Camilo']
historia_usuarios = ['Andres']

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        usr = escape(request.form['usrtxt'])
        clv = escape(request.form['pwdtxt'])
        if usr in lista_usuarios:
            return f"Suministro los siguientes datos {usr} y {clv}"
        else:
            return f"Error en usuario o clave"

## TODO: Arreglar validaciones y mirar como se puede usar null para verificacion de datos en inputs.

@app.route('/registrar', methods=['GET','POST']) 
def registrar():
    if request.method == 'GET':
        return render_template('registrar.html')
    else:
        T_DNI = escape(request.form['t_dnitxt'])
        DNI = escape(request.form['dnitxt'])
        USR = escape(request.form['usrtxt'])
        GNR = escape(request.form['gnrtxt'])
        CIU = escape(request.form['ciutxt'])
        EMAIL = escape(request.form['emailtxt'])
        PSW = escape(request.form['pswtxt'])
        R_PSW = escape(request.form['r_pswtxt'])
        if T_DNI != '':
            return f"Se registro el usuario con exito"

 ## rutas paciente   


@app.route('/dashboardPacientes', methods=['GET']) 
def dashboardPacientes():
    return render_template('dashboardPacientes.html')

@app.route('/agendarCita', methods=['GET','POST'])
def agendarCita():
    return render_template('agendarCitas.html')

@app.route('/HistoriaClinica/<id_usuario>', methods=['GET','POST'])
def historiaClinica(id_usuario):
    if id_usuario in historia_usuarios:
        return render_template('historiaClinicaPaciente.html')
    else:
        return f"El usuario no cuenta aun con historia clinica"

## end rutas paciente

## rutas medicos

@app.route('/dashboardMedico', methods=['GET'])
def dashboardMedico():
    return render_template('dashboardMedico.html')

@app.route('/citasProgramadas', methods=['GET'])
def verCitasProgramadas():
    return render_template('verCitasProgramadas.html')

@app.route('/detallePacientes', methods=['GET'])
def verListaPacientes():
    return render_template('verListadoPacientes.html')

## end rutas medicos

## rutas admin

@app.route('/dashboardAdmin', methods=['GET'])
def dashboardAdmin():
    return render_template('dashboardAdmin.html')

@app.route('/verCitas', methods=['GET'])
def verCitasAdmin():
    return render_template('verCitas_Admin.html')

@app.route('/verUsuarios',methods=['GET'])
def verUsuarios():
    return render_template('verListadoUsuarios.html')

## end rutas admin

## rutas perfiles de usuarios

@app.route('/perfil', methods=['GET'])
def verPerfil():
    return render_template('perfil_admin.html')

@app.route('/configuracionUsuario',methods=['GET','POST'])
def configUsuario():
    return render_template('config_admin.html')

## end ruta perfiles de usuarios

@app.route('/registrar') 
def registrar():
    return render_template('registrar.html') 

@app.route('/dashboardPacientes') 
def dashboardPacientes():
    return render_template('dashboardPacientes.html')

@app.route('/agendarCita') 
def agendarCita():
    return render_template('agendarCita.html')

@app.route('/historiaClinica') 
def historiaClinica():
    return render_template('historiaClinica.html')

@app.route('/perfilPaciente') 
def perfilPaciente():
    return render_template('perfilPacientes.html')

@app.route('/configuracionPaciente') 
def configuracionPaciente():
    return render_template('configuraconPacientes.html')            


app.run(debug=True)    
