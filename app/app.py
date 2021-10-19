from flask import Flask,render_template
app =  Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

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
