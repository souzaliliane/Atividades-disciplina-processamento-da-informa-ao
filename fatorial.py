#Cálculo fatorial

n = int(input("Digite um número para calcular seu fatorial"))
fat = 1
for c in range(n,0,-1):
    fat = fat * c

print(f'{n}!={fat}')
