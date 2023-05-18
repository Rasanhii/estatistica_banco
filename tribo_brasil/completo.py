from conexao import conectar

def listar(conn, cursor):
    # Abrir uma conexão com o vvanco de dados
    conn = conectar()
    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()
    # executar a consulta SQL para listar os registros
    cursor.execute("SELECT * FROM tribo")
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
    sql = 'INSERT INTO tribo (nome_tribo, num_hab, renda_mensal, escolaridade, trab_salar) VALUES (%s, %s, %s, %s, %s)'
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
    sql = 'DELETE FROM tribo WHERE id = %s'
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


def atualizar(nome_tribo, num_hab, renda_mensal, escolaridade, trab_salar):
    # Abrir uma conexão com o banco de dados
    conn = conectar()

    # Criando um objeto cursor para executar as consultas SQL
    cursor = conn.cursor()

    # Executar a consulta SQL para atualizar o registro
    sql = "UPDATE tribo SET nome_tribo = %s, num_hab= %s, renda_mensal= %s, escolaridade= %s, trab_salar = %s WHERE id = %s"
    val = (nome_tribo, num_hab, renda_mensal, escolaridade, trab_salar)
    cursor.execute(sql, val)

    # Commit da transação
    conn.commit()

    # Verificar se algum registro foi atualizado
    if cursor.rowcount == 0:
        print("Nenhum registro atualizado.")
    else:
        print("Registro atualizado com sucesso.")

    # Fechar a conexão e o cursor
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
  print("4 - Atualizar uma tribo")
  print("0 - Sair")
  
  opcao = int(input("Digite o número da opção desejada: "))

  if opcao == 1:
    # Listar tribos
    listar(conn, cursor)
  
  elif opcao == 2:
    # Inserir novo tribo
    nome_tribo = input("Digite nome da nova tribo: ")
    num_hab = int(input("Digite o num de habitantes da nova tribo: "))
    renda_mensal = input("Digite a renda mensal: ")
    escolaridade = input("Digite a escolaridade da nova tribo: ")
    trab_salar = input("Digite se possuem trabalho assalariado: ")
    
    inserir(nome_tribo, num_hab, renda_mensal, escolaridade, trab_salar)

  elif opcao == 3:
    # Deletar um tribo
    codigo = int(input("Digite o código da tribo que deseja deletar: "))
    deletar(codigo)


  elif opcao == 4:
    # Atualizar um tribo
    nome_tribo = input("Digiteo nome da nova tribo: ")
    num_hab = int(input("Digite o num de habitantes da nova tribo: "))
    renda_mensal = input("Digite a renda mensal: ")
    escolaridade = input("Digite a escolaridade da nova tribo: ")
    trab_salar = input("Digite se possuem trabalho assalariado: ")
    atualizar(nome_tribo, num_hab, renda_mensal, escolaridade, trab_salar)
  

  elif opcao == 0:
    # Sair do programa
    break

  else:
    print("Opção inválida. Digite novamente.")
    
# Fechar a conexão e o cursor
cursor.close()
conn.close()