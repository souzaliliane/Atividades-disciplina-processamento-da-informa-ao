#6 - Capture nomes do teclado, encerre o programa quando o tamanho do nome for maior que 20

while True:
    nome = input('Digite um nome ')
    tam = len(nome)
    if tam > 20:
        break
print(f'\33[1;31m PAROU!!! \33[m\n Você digitou o nome:\33[5;49;34m {nome} \33[m\n que tem \33[5;49;33m {tam} \33[m caracteres!' )
