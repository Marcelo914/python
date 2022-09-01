n = int(input("digite o numero para achar seu valor fatorial: "))
qnt = n
while qnt > 1:
    n = n * (qnt-1)
    qnt = qnt - 1
print (n)