import sqlite3

# Conectar ao banco de dados (ou criar o arquivo se não existir)
conn = sqlite3.connect('banco_de_dados.db')

# Criar a tabela 'usuarios'
conn.execute('''CREATE TABLE usuarios
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT NOT NULL,
                 email TEXT NOT NULL,
                 senha TEXT NOT NULL);''')

# Fechar a conexão com o banco de dados
conn.close()

print('Banco de dados criado com sucesso!')
