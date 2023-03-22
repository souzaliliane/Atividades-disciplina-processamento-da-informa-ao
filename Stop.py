#Stop André

while True:
    nome = input('Digite um nome ')
    nome = nome.upper() #tratando a string para deixa-la toda maiúscula
    if nome == "ANDRE" or nome == "ANDRÉ":
        break

print(f' Finalmente você digitou {nome}')
