import bcrypt

senha = input("Digite sua senha: ").encode()

hash = bcrypt.hashpw(senha, bcrypt.gensalt())
print("Hash gerado:", hash.decode())

senha_verif = input("Digite novamente para verificar: ").encode()
if bcrypt.checkpw(senha_verif, hash):
    print("Senha correta!")
else:
    print("Senha incorreta!")
