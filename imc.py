# Calculadora de índice de massa corpórea python.
# Feito por João Lucas, 04/08/2022.
# imc menor que 18,5 = magro
# imc entre 18,5 e 24,9 = normal
# imc entre 25,0 e 29,9 = sobrepeso
# imc entre 30,0 e 39,9 = obesidade
# imc maior que 40 = obesidade grave


peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso // (altura ** 2)

if imc <= 18.5:
    print('Você é magro, ' + 'seu imc mede ' + str(imc))

elif imc <= 18.5 or imc <= 24.9:
    print('Você está com o peso normal, ' + 'seu imc mede ' + str(imc))

elif imc <= 25.0 or imc <= 29.9:
    print('Você está acima do peso normal, ' + 'seu imc mede ' + str(imc) + '\nPara atingir o seu peso ideal, você '
                                                                            'deve '
                                                                            'pesar entre 41.6 e 56kg.')

elif imc <= 24.9 or imc <= 30.0:
    print('Você está com pré-obesidade, ' + 'seu imc mede ' + str(imc) + '\nPara atingir o seu peso ideal, você deve '
                                                                         'pesar entre 41.6 e 56kg.')

elif imc > 30.0:
    print('Você está com obesidade, ' + 'seu imc mede ' + str(imc) + '\nPara atingir o seu peso ideal, você deve '
                                                                     'pesar entre 41.6 e 56kg.')

else:
    print('Você digitou um valor muito alto')
