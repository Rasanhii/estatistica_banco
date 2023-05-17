import mysql.connector

def conectar():
    mybd = mysql.connector.connect(
        host = 'ativ-brasil.cddn3xpihyde.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password = 'aulanoite',
        database = 'tribos_brasileiras'
    )
    return mybd