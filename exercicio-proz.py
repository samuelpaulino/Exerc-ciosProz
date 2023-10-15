#Precisamos imprimir um número para cada andar de um hotel de 20 andares.
#Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.
#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.
#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

#Utilizando o laço while:
andar_atual = 1
while andar_atual <= 20:
    if andar_atual == 13:
        andar_atual += 1
        continue
    print("ANDAR:",andar_atual)
    andar_atual += 1

#Utilizando a função range() em ordem decrescente de andares:
for andar in range(20,0,-1):
    if andar == 13:
        continue
    print("Andar:", andar)

andar = 20
while (andar > 0):
    if andar == 13:
        andar -= 1
    print("Andar:", andar)
    andar = andar - 1