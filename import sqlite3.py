import sqlite3

# Conectar ao banco de dados (ou criar o arquivo se não existir)
conn = sqlite3.connect('rpg.db')

# Criar a tabela 'usuarios'
conn.execute('''CREATE TABLE personagens
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT NOT NULL,
                 vida TEXT NOT NULL,
                 cd TEXT NOT NULL);''')

# Fechar a conexão com o banco de dados
conn.close()

print('Banco de dados criado com sucesso!')
