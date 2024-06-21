import sqlite3

# Conectar ao banco de dados (ou criar o arquivo se não existir)
conn = sqlite3.connect('rpg.db')

# Criar a tabela 'Personagens'
# conn.execute('''CREATE TABLE personagens
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                  nome TEXT NOT NULL,
#                  vida TEXT NOT NULL,
#                  cd TEXT NOT NULL);''')

# Criar a tabela 'Battles'
conn.execute('''CREATE TABLE battles
                (id INTEGER PRIMARY KEY AUTOINCREMENT,                                  
                 battle_name TEXT NOT NULL);''')


# Fechar a conexão com o banco de dados
conn.close()

print('Banco de dados criado com sucesso!')
