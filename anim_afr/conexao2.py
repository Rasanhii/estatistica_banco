import mysql.connector

# Definir as informações de conexão
config = {
  'user': 'usuarioremoto',
  'password': 'minhasenha',
  'host': '100.26.22.143',
  'database': 'anim_africa'
}

# Estabelecer a conexão com o banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")
# Fechar a conexão
conn.close()


import mysql.connector

def conectar():
    mybd = mysql.connector.connect(
        host = '100.26.22.143',
        user = 'usuarioremoto',
        password = 'minhasenha',
        database = 'anim_africa'
    )
    return mybd