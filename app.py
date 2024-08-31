from flask import Flask,request,render_template,flash,url_for,redirect

app = Flask(__name__)
app.secret_key = 'mysecretkey'


@app.route('/administrador')
def administrador():
    return render_template('administrador.html')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/registroMedicos')
def registroMedicos():
    return render_template('registroMedicos.html')

if __name__ == '__main__':
       app.run(port=3000,debug=True)
