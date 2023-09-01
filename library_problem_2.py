def divisao():

    x = 20
    y = 10

    if x > y:
        x,y = y,x
        
    numeros = []
    for i in range(x+1, y):
        if i % 5 == 2 or i % 5 == 3:
            numeros.append(i)

    print("Os números são..: {}".format(" ".join(str(n) for n in numeros)))
