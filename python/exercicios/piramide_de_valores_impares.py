"""
loop entrada - 1
    quant + 2
    loop range()

3 5 7 
9 11 13 15 17

atual + 2 * quant

"""

def somaDois(x):
    return x+2

#Obtem o primeiro numero da linha
def obterNumeroInicial(numero_itens, numero_atual):
    
    #for y in range(0, numero_itens):
    #    numero_atual = somaDois(numero_atual)
    numero_atual = numero_atual + (numero_itens*2)

    return numero_atual

#Obtem o somatorio dos 3 ultimos numeros da linha
def obtemSomatorio(numero_itens, numero_atual):
    somatorio = 0

    for y in range(0, numero_itens):
        numero_atual = somaDois(numero_atual)
        if(y+3 >= numero_itens):
            somatorio += numero_atual
        else:
            continue

    return somatorio

#Obtem o somatorio dos 3 ultimos numeros da linha de forma ainda mais rapida e simples
def obtemSomatorioSimples(numero_itens, numero_atual):
    
    ultimo_numero = numero_atual + (numero_itens*2)

    somatorio = ultimo_numero + (ultimo_numero - 2) + (ultimo_numero - 4)

    return somatorio

#Percorre as linhas e retorna o somatorio da linha desejada
def somatorioDesejado(numero_linhas_esperado):

    numero_inicial = 1
    numero_itens = 1

    for i in range(1, int(numero_linhas_esperado)-1): 
        numero_itens = somaDois(numero_itens)
        numero_inicial = obterNumeroInicial(numero_itens, numero_inicial) 
    
    #soma_tres_ultimos = obtemSomatorio(numero_itens+2, numero_inicial) 
    soma_tres_ultimos = obtemSomatorioSimples(numero_itens+2, numero_inicial) 

    return soma_tres_ultimos

def main(numero_linhas_esperado):

    if(type(numero_linhas_esperado) != int):
        print("Nesse programa nao eh aceito \'"  + str(numero_linhas_esperado) + "\' como entrada!")

    elif(numero_linhas_esperado <= 1 or numero_linhas_esperado > 10000000):
        print("Numero de linhas "  + str(numero_linhas_esperado) + " diferente da aceita pelo programa!")
        
    else:
        soma = somatorioDesejado(numero_linhas_esperado)
        print(soma)
        return soma

if __name__ == "__main__":
    
    try:
        main(1) 
        main(2) #15
        main(3) #45
        main(4) #87
        main(5) #141
        main(100) #59991
        main(233) #325725
        main("a")
        main(10000000) #599999999999991
    except Exception as e:
        print("Exception = " + str(e))