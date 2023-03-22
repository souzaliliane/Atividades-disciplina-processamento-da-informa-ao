# 4 - Capture um número (N) do teclado,
# imprima todo os múltiplos de 11 ou 13 entre 0 e N (número  digitado)

n = int(input(' Digite um número ...'))
c = 0
print(f' Múltiplos de 11 ou 13 entre 0 e {n} :')

for c in range (0, n):
    if c % 11 ==0 or c % 13 ==0:
        print(c, end= ' ')
    c += 1
