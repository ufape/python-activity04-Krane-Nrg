def media ():

    N1 = float(input("Digite a nota 1: "))
    N2 = float(input("Digite a nota 2: "))
    N3 = float(input("Digite a nota 3: "))
    N4 = float(input("Digite a nota 4: "))
    media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

    if media >= 7.0:
        print(f"Media: {media:.1f}")
        print("Aluno aprovado.")
    else:
        print(f"Media: {media:.1f}")
        print("Aluno em exame.")
        exame = float(input("Digite a nota do exame: "))
        nova_media = (media + exame)/2
        if nova_media >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        print(f"Media final: {nova_media:.1f}")
        
