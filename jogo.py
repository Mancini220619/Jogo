import random

print('#####################')
print('#ask to oraculo game#')
print('#####################')

sequencia_numerica = random.randrange (1,101) #gera numeros aleatorios de 1, 101
print(type(sequencia_numerica))
numero_jogadas = 0
points = 850

print ("Qual nivel de dificuldade?")
print ('(1) Fácil (2) Médio (3) Difícil')
nivel = int (input("selecione o nivel: "))

if nivel == 1:
    numero_jogadas = 17
elif nivel == 2:
    numero_jogadas = 9
else:
    numero_jogadas = 4

for round in range (1, numero_jogadas + 1):
    print ('jogada {} de {}'.format(round, numero_jogadas))
    tentativa = int (input ('adivinhe a sequencia numerica, digite um numero: '))
    print ('voce digitou ', tentativa)

    if tentativa < 1 or tentativa > 100:
        print('o numero deve estar entre 1 e 100!')
        continue

    adivinhou = tentativa == sequencia_numerica
    numero_maior = tentativa > sequencia_numerica
    numero_menor = tentativa < sequencia_numerica

    if tentativa <1 or tentativa> 100:
        print('o numero de estar entre 1 e 100')
        continue

    adivinhou = tentativa == sequencia_numerica
    numero_maior = tentativa > sequencia_numerica
    numero_menor = tentativa < sequencia_numerica

    if adivinhou:
        print("Adivinhou, Parabéns!!!")
        break
    else:
        if numero_maior:
            print("sua sugestao foi maior que a sequencia numerica")
        elif numero_menor:
            print("sua sequencia foi menor que a sequencia numerica")
        print("infelizmente, voce não acertou.")
        lost_points = abs(sequencia_numerica - tentativa)
        points = points - lost_points
    print("-------------------")
print("Game Over")