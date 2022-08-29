# Calculadora de índice de massa corpórea python.
# Feito por João Lucas, 04/08/2022, Versão 1.0
# imc menor que 18,5 = magro
# imc entre 18,5 e 24,9 = normal
# imc entre 25,0 e 29,9 = sobrepeso
# imc entre 30,0 e 39,9 = obesidade

while True:
    try:
        print("Calculadora python imc.")
        opc = int(input("Seja bem vindo/a!\nPressione 1 para calcular.\nPressione 2 para ajuda.\nPressione 3 para "
                        "fechar o programa.\n"))

        if opc == 1:
            pass
        elif opc == 2:
            print("Ao inserir o peso, evite letras, e ao inserir a altura não esqueça de colocar o ponto entre o "
                  "metro e cm.")
            pass
        elif opc == 3:
            break
        else:
            print("Você digitou uma opção incorreta, tente novamente.\n")
            continue

    except ValueError:
        print("erro: Você digitou uma letra, tente novamente com números!\n")
        continue

    try:
        peso = int(input("Digite seu peso: "))
        altura = float(input("Digite sua altura: "))
        if altura == int(altura):
            print("\nTente inserir a altura em número decimal.\n")

            continue
        imc = peso // (float(altura) ** 2)

        if imc <= 18.5:
            print("Você é magro, " + "seu imc mede " + str(imc) + '.\n')

        elif imc <= 18.5 or imc <= 24.9:
            print("Você está com o peso normal, " + "seu imc mede " + str(imc) + '.\n')

        elif imc <= 25.0 or imc <= 29.9:
            print("Você está acima do peso normal, " + "seu imc mede " + str(imc) + "\nPara atingir o seu peso "
                                                                                    "ideal, "
                                                                                    "você "
                                                                                    "deve "
                                                                                    "pesar entre 41.6 e 56kg.\n")

        elif imc <= 24.9 or imc <= 30.0:
            print('Você está com pré-obesidade, ' + 'seu imc mede ' + str(imc) + "\nPara atingir o seu peso "
                                                                                 "ideal, você deve "
                                                                                 "pesar entre 41.6 e 56kg.\n")
        elif imc > 30.0:
            print('Você está com obesidade, ' + 'seu imc mede ' + str(imc) + "\nPara atingir o seu peso ideal, "
                                                                             "você deve "
                                                                             "pesar entre 41.6 e 56kg.\n")

    except ValueError:
        print("erro: Você digitou uma letra, tente novamente com números!\n")
