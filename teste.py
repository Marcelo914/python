if delta < 0:
    print ("Essa equação não possui raizes reais.")
if delta > 0:
    x1 = (-B + math.sqrt(delta))/2*A
    x2 = (-B - math.sqrt(delta))/2*A
    print("As raizes da equação são:", float(x1), "e" ,  float(x2) )