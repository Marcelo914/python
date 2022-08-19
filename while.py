from math import prod

produto = 1

valor = 1
qnt = int(input("digite o tamanho da sequencia a ser somada: "))
if qnt == 0:
    print("multiplicação por 0 sempre será 0")
else:

    while qnt > 0:
        valor = int(input("digite o valor a ser somado: "))
        qnt = qnt - 1
        produto = produto * valor
    print ("A soma final é: ", produto)   


 