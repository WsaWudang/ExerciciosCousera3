#Receba um número inteiro positivo na entrada e imprima os  n n primeiros números ímpares naturais.

n = int(input("Digite o valor de n: "))
i = 0
impar = 1

while i < n:
	print(impar)
	i = i + 1
	impar = impar + 2