# 3  – Capture um número (N) do teclado imprima  todo os números pares entre 0 e N

n = int(input('Digite um número '))
c=0
print(f'Os números pares entre {n} e 0:')
for c in range (0,n):

    if c % 2 == 0:
        print(c, end=' ')
    c +=1
