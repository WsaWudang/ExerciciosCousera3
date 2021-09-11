# Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.

n = int(input("Digite ovalor de n: "))
fatorial = 1

while (n > 0 ):
	fatorial = fatorial * n
	n -= 1

print(fatorial)