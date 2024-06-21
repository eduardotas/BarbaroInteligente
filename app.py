from flask import Flask, request, jsonify, redirect, render_template, url_for
import sqlite3

db = 'rpg.db'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def page_cadastro():
    return render_template('cadastro.html')

@app.route('/consulta')
def consulta():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM personagens')
    personagens = cursor.fetchall()
    conn.close()

    return render_template('consulta.html', personagem=personagens)

@app.route('/page_editar/<int:id>', methods=['GET', 'POST'])
def page_editar(id):    
    # carregar os dados do registro do banco de dados
    with sqlite3.connect(db) as con:
        cur = con.cursor()
        cur.execute('SELECT * FROM personagens WHERE id=?', (id,))
        data = cur.fetchone()

    # renderizar a página de edição com os dados do registro
    return render_template('editar.html', data=data)

@app.route('/editar', methods=['GET', 'POST'])
def editar():
    # obter os dados do formulário
    id = request.form['id']
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['senha']

    # atualizar o registro no banco de dados
    with sqlite3.connect(db) as con:
        cur = con.cursor()
        cur.execute('UPDATE personagens SET nome=?, vida=?, cd=? WHERE id=?', (nome, email, telefone, id))
        con.commit()

    # redirecionar para a página de consulta
    return redirect(url_for('consulta'))

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = request.form
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO personagens (nome, vida, cd) VALUES (?, ?, ?)',
                   (dados['nome'], dados['vida'], dados['cd']))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/excluir/<int:id>')
def excluir(id):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM personagens WHERE id=?', (id,))
    conn.commit()
    conn.close()

    return redirect('/consulta')


if __name__ == '__main__':
    app.run(debug=True)

