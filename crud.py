import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conectar():
    con = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield con
    finally:
        print('Conexão fechada')
        con.close()

# def consulta(campo, banco):
#     consulta=f'SELECT {campo} FROM {banco}'
#     return consulta



'''conexão para inserir dados'''
with conectar() as conexao:
    with conexao.cursor() as cursor:
        sql_command ='INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
                     '(%s, %s, %s ,%s)'
        dados = [
            ("Muriel", "Figueiredo", "19", "55"),
            ("Roel", "Figueiredo", "19", "55"),
            ("Jose", "Figueiredo", "19", "55")
        ]
        cursor.executemany(sql_command, dados)
        conexao.commit()

# '''conexão para apagar dados'''
# with conectar() as conexao:
#     with conexao.cursor() as cursor:
#         sql_command = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql_command, (6,))
#         conexao.commit()

'''conexão para apagar dados'''
with conectar() as conexao:
    with conexao.cursor() as cursor:
        # sql_command = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
        sql_command = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
        cursor.execute(sql_command, (10,12))
        conexao.commit()


'''conexão para atualizar tabela'''
with conectar() as conexao:
    with conexao.cursor() as cursor:
        sql_command = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql_command, ('JOANA', 5))
        conexao.commit()



# '''conexão para inserir dados'''
# with conectar() as conexao:
#     with conexao.cursor() as cursor:
#         sql_command ='INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#                      '(%s, %s, %s ,%s)'
#         cursor.execute(sql_command, ('Jack', 'Moroe', 112, 220))
#         conexao.commit()

with conectar() as conexao:

    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM clientes")
        # cursor.execute("SELECT * FROM clientes.clientes")   //utiliza-se essa opção, caso não tenha passado o banco de
        # dados na conexão

        def consulta(campo, banco, *args):
            dados = f'SELECT {campo} FROM {banco}'
            cursor.execute(dados)
            for i in cursor.fetchall():
                print(i[campo])

        # consulta('nome', 'clientes')

        # cursor.execute('SELECT nome as nome, sobrenome as sn FROM clientes LIMIT=100')
        # resultado = cursor.fetchall()
        #
        # for i in resultado:
        #     print(i['n'], i['sn'])

        # cursor.execute('SELECT nome, sobrenome FROM clientes ORDER BY id DESC LIMIT 100')
        cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 100')
        resultado = cursor.fetchall()

        for i in resultado:
            print(i)









