import math

def adicao (a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida")
    return a / b

def fatorial(n):
    if n < 0:
        raise ValueError("Fatorial não está definido para números negativos")
    return math.factorial(n)

def pontecia(base, expoente):
    return base ** expoente

def menu():
    print("Selecione a operacao:")
    print("1. adicao")
    print("2. subtracao")
    print("3. multiplicacao")
    print("4. divisao")
    print("5. fatorial")
    print("6. potencia")

while True:
    menu()
    
    escolha = input("Digite sua escolha (1/2/3/4/5/6): ")
    
    if escolha in ['1', '2', '3', '4', '6']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if escolha == '1':
            print(f"Resultado: {adicao(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif escolha == '4':
            print(f"Resultado: {divisao(num1, num2)}")
        elif escolha == '6':
            print(f"Resultado: {pontecia(num1, num2)}")
    
    elif escolha == '5':
        num = int(input("Digite o número para o fatorial: "))
        print(f"Resultado: {fatorial(num)}")
    
    else:
        print("Opção inválida!")

    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break


