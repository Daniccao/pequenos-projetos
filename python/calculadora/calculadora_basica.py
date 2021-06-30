def main():

    tipoOperacao = operacao()

    numValores = list(valores(tipoOperacao))

    if(int(tipoOperacao) == 1):
        soma = lambda valor: int(valor[0]) + int(valor[1])
        print("\n")
        print(str(numValores[0]) + " + " + str(numValores[1]) + " = " + str(soma(numValores)))
        print("\n")
    elif(int(tipoOperacao) == 2):
        subtracao = lambda valor: int(valor[0]) - int(valor[1])
        print("\n")
        print(str(numValores[0]) + " - " + str(numValores[1]) + " = " + str(subtracao(numValores)))
        print("\n")
    elif(int(tipoOperacao) == 3):
        multipicacao = lambda valor: int(valor[0]) * int(valor[1])
        print("\n")
        print(str(numValores[0]) + " * " + str(numValores[1]) + " = " + str(multipicacao(numValores)))
        print("\n")
    elif(int(tipoOperacao) == 4):
        divisao = lambda valor: int(valor[0]) / int(valor[1])
        print("\n")
        print(str(numValores[0]) + " / " + str(numValores[1]) + " = " + str(divisao(numValores)))
        print("\n")
    else:
        print("Ocorreu algum problema, tente novamente!")

    return 0    

def operacao():

    entradaOperacao = operacaoEntradaManual()
    #entradaOperacao = operacaoEntradaAutomatica()

    return entradaOperacao

def operacaoEntradaManual():

    print('Operações fornecidas:\n\n'
        + "1 - Soma\n"
        + "2 - Subtração\n"
        + "3 - Multiplicação\n"
        + "4 - Divisão\n")
    
    operacao = input("Qual operação deseja realizar? ")
    print("\n")

    if(int(operacao) > 4 or int(operacao) < 1):
        print("\n\nOperação não valida!\n"
            + "Por favor, insira o valor novamente!\n")

        operacaoEntradaManual()
    else:
        return operacao

def valores(tipoOperacao):

    entradaValores = valoresEntradaManual(tipoOperacao)
    #entradaValores = valoresEntradaAutormatica(tipoOperacao)

    return entradaValores

def valoresEntradaManual(tipoOperacao):

    valor1 = input("Insira o primeiro valor: ")
    valor2 = input("Insira o segundo valor: ")
    
    if(int(valor2) == 0 and int(tipoOperacao) == 4):
        while(int(valor2) == 0):
            print("\nNao eh possivel divisão por 0!")
            valor2 = input("Insira o segundo valor novamente: ")

    return [valor1, valor2]



if __name__ == '__main__':
    main()