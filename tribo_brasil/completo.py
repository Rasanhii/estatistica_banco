from conexao import conectar

def listar(conn, cursor):
    # Abrir uma conexão com o vvanco de dados
    conn = conectar()
    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()
    # executar a consulta SQL para listar os registros
    cursor.execute("SELECT * FROM tribos_brasileiras")
    #obter os resultados
    resultados = cursor.fetchall()
    # imprimir os resultados
    for resultado in resultados:
        print(resultado)
    # fechar a conexão e o cursor
    cursor.close()
    conn.close()
    
    
def inserir(nome_tribo, num_hab, renda_mensal, escolaridade, trab_salar):
    # Abrir uma conexão com o vvanco de dados
    conn = conectar()
    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()
    # executar a consulta SQL para listar os registros
    sql = 'INSERT INTO tribos_brasileiras (nome_tribo, num_hab, renda_mensal, escolaridade, trab_salar) VALUES (%s, %s)'
    val = (nome_tribo, num_hab, renda_mensal, escolaridade, trab_salar)
    cursor.execute(sql, val)
    #commit da transação
    conn.commit()
    #imprimir mensagens de sucesso
    print('Registro inserido com sucesso.')
    #imprimir a conexão e o cursor
    cursor.close()
    conn.close()

def deletar(codigo):
    # Abrir uma conexão com o vvanco de dados
    conn = conectar()
    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()
    # executar a consulta SQL para listar os registros
    sql = 'DELETE FROM tribos_brasileiras WHERE codigo = %s'
    val = (codigo,)
    cursor.execute(sql, val)
    #commit da transação
    conn.commit()
    
    if cursor.rowcount == 0:
        print('Nenhum registro deletado.')
    else:
        print('Registro deletado com sucessor')
    #fechar a conexão e o cursor
    cursor.close()
    conn.close()

conn = conectar()

cursor = conn.cursor()

while True:
  # Mostra as opções de operação
  print("O que você deseja fazer?")
  print("1 - Listar tribos")
  print("2 - Inserir nova tribo")
  print("3 - Deletar uma tribo")
  print("0 - Sair")
  
  opcao = int(input("Digite o número da opção desejada: "))

  if opcao == 1:
    # Listar estados
    listar(conn, cursor)
  
  elif opcao == 2:
    # Inserir novo estado
    nome_tribo = input("Digite nome da nova tribo: ")
    num_hab = int(input("Digite o num de habitantes da nova tribo: "))
    renda_mensal = input("Digite a renda mensal: ")
    escolaridade = input("Digite a escolaridade da nova tribo: ")
    trab_salar = input("Digite se possuem trabalho assalariado: ")
    
    inserir(nome_tribo, num_hab, renda_mensal, escolaridade, trab_salar)

  elif opcao == 3:
    # Deletar um estado
    codigo = int(input("Digite o código da tribo que deseja deletar: "))
    deletar(codigo)

  elif opcao == 0:
    # Sair do programa
    break

  else:
    print("Opção inválida. Digite novamente.")
    
# Fechar a conexão e o cursor
cursor.close()
conn.close()