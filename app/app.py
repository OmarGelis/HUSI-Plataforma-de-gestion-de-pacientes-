from flask import Flask,render_template
app =  Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboardPacientes') 
def dashboardPacientes():
    return render_template('dashboardPacientes.html')

@app.route('/registrar') 
def registrar():
    return render_template('registrar.html')        

app.run(debug=True)    
