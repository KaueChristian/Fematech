from flask import Flask, render_template, request, session, flash, redirect
import yanderer
app = Flask(__name__)

# Defina uma chave secreta única e segura
app.config['SECRET_KEY'] = 'peripecias69'

# Inicializa uma lista de usuários
users_data = []

# Modelagem de usuário
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Rotas
@app.route('/')
def index():
    if session.get('logged_in'):
        return render_template('home.html')
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Procura o usuário na lista
        user = next((u for u in users_data if u['username'] == username), None)

        if user and user['password'] == password:
            # Usuário autenticado
            session['logged_in'] = True
            session['username'] = username
            return redirect('/')
        else:
            # Usuário não autenticado
            flash('Usuário ou senha inválidos.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    # Exemplo de inicialização com um usuário pré setado
    initial_user = {
        "username": "teste",
        "password": "1234"
    }
    users_data.append(initial_user)

    app.run(debug=True)
