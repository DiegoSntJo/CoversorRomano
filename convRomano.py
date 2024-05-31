#Importando biblioteca math para o algoritmo
import math

#Função para conversão dos números
def converterRomano(A):
    #Principais algarismos são armazenados em uma variável
    algRomano = {1: "I",5: "V",10: "X",50: "L",100: "C",500: "D",1000: "M",5000: "G",10000: "H"}
    
    #Principal dígito significativo é extraído
    div = 1
    while A >= div:
        div *= 10
  
    div /= 10
  
    res = ""
  
    while A:
        
        #Dígito principal inserido na variável ultNum
        ultNum = int(A / div)

        #Verifica se o dígito é menor ou igual a três
        if ultNum <= 3:
            res += (algRomano[div] * ultNum)
        #Verifica se o dígito é igual a quatro
        elif ultNum == 4:
            res += (algRomano[div] +
                        algRomano[div * 5])
        #Verifica se o dígito é menor ou igual a oito
        elif 5 <= ultNum <= 8:
            res += (algRomano[div * 5] +
            (algRomano[div] * (ultNum - 5)))
        #Verifica se o dígito é igual a nove
        elif ultNum == 9:
            res += (algRomano[div] +
                        algRomano[div * 10])

        A = math.floor(A % div)
        div /= 10
          
    return res

#Função para conversão dos algarismos
def converterInteiro(input):
    #Transforma em maiuscúlo
    input = input.upper( )

    #Variável que armazena algarismos
    nums = {'M':1000,
             'D':500,
             'C':100,
             'L':50,
             'X':10,
             'V':5,
             'I':1}
    
    #Variável de retorno
    sum = 0

    #Separando e convertendo inteiro
    for i in range(len(input)):
        value = nums[input[i]]
        if i+1 < len(input) and nums[input[i+1]] > value:
            sum -= value
        else: sum += value
     
    return sum

#Chamando função de coversão para algarismos romanos
def chamarRomano():
    #Entrada do número para conversão
    valor = int(input("\nDigite um numero de 1 a 1000 para ser convertido: "))

    if valor < 1 or valor > 1000:
        #Verificar se é um número válido
        print("Digite um numero de válido.")
    else:
        #Saída do número convertido
        print("\nValor convertido para Romano: "+ str(converterRomano(valor)))

#Chamando função de coversão para números inteiros
def chamarInteiro():
    #Entrada do algarismo para conversão
    valor = input("\nDigite o algarismo a ser convertido: ")
    converterInteiro(valor)

    #Saída do algarismo convertido
    print("\nValor convertido para Inteiro: "+ str(converterInteiro(valor)))

#Variável para estrutura de repetição infinita
i = 1

#Estrutura de repetição infinita
while i != 0:
    #Selecionar opção
    print("\n1. Inteiro para romano")
    print("2. Romano para inteiro")
    opSele = int(input("Escolha a forma de conversão: "))

    #Estrutura condicional da opção selecionada
    if opSele == 1:
            chamarRomano()
    elif opSele == 2:
            chamarInteiro()
    else:
        print("Digite uma das opções válidas\n")

