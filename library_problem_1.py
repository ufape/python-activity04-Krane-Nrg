def media ():

    N1 = 2.0
    N2 = 3.0
    N3 = 4.0
    N4 = 1.0
    media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

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
        
