import mysql.connector


connect = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Joao1908.',
    database='atvcrud',
)

cursor = connect.cursor()
new_user = input('Você é um novo usuário? (Sim ou Não)')
if new_user.lower() == 'sim':
    usuario = input("Insira seu nome de usuário para o cadastro: ")
    senha = input("Insira sua senha para cadastro: ")
    recuperacao = input("Insira um código para recuperação em caso de esquecimento de senha.")
    # Create
    command = f'INSERT INTO login (User, Senha, senha_de_recuperacao) VALUES ("{usuario}", "{senha}", "{recuperacao}")'
    cursor.execute(command)
    connect.commit() # Atualiza/edita o banco de dados

if new_user.lower() == 'não':
# Read

    usuario = input("Insira seu nome de usuário: ")
    senha = input("Insira sua senha: ")
    command = f'SELECT Senha FROM login WHERE User = "{usuario}"' # Que diabo pra arrumar isso aqui sem dar none, vsf, nunca mais pego pra fazer essa porra.
    cursor.execute(command)
    resultado = cursor.fetchone() # Armazena as informações / Lê o banco de dados
    
    if resultado is None:
        print('Usuário não encontrado.')
    
    elif senha != resultado[0]:
       print("As informações não coincidem com o que está em nosso sistema.")
    
    else:
        print("Login bem sucedido!")

#Update
    if resultado is None:
        pass
    elif senha != resultado[0]:
        forgot = input('Deseja recuperar sua senha? (Será necessário o código de recuperação inserido no cadastro) ')
        
        if forgot.lower() == 'sim':
            codigo = input('Insira seu código de recuperação: ')
            command = f'SELECT senha_de_recuperacao FROM login WHERE User = "{usuario}"'
            cursor.execute(command)
            res = cursor.fetchone()

            if codigo != res[0] and res != None:
                print("A senha de recuperação está errada.")

            elif codigo == res[0] and res != None:
                novasenha = input("Insira sua nova senha: ")
                command = f'UPDATE login SET Senha = "{novasenha}" WHERE User = "{usuario}"'
                cursor.execute(command)
                connect.commit()
                print('Senha atualizada com sucesso!')

            else:
                print('Usuário não encontrado para a recuperação.')

        else:
            print("Até a próxima!")
    


cursor.close()
connect.close()