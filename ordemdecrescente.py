decrescente = True
anterior = int(input("digite o primeiro numero da sequencia: "))
valor = 1

while valor != 0 and decrescente:
    valor = int(input("digite os proximos numeros da sequencia: "))
    if valor > anterior:
        decrescente = False
    anterior = valor
if decrescente:
    print("A sequencia esta em ordem decrescente!")
else:
    print("A sequencia não ta em ordem decrescente")