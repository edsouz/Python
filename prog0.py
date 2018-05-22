a = int(input("Digite um número inteiro: "))
b = int(input("Digite um outro número inteiro: "))

def soma(x,y):
    return x + y

s = soma(a,b)

print(" ")
print(" ======================================== ")
print("o primeiro número digitado foi %d\n" %a)
print("O segundo número digitado foi %d\n" %b)
print("A soma dos números digitados é %d" %s)
print(" ======================================== ")
print(" ")

if s > 10:
    print("\nO valor é maior que 10!\n")
else:
    print("O valor não é maior que 10!\n")







