def menu():
    print("\nCalculadora Simples")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro! Não é possível dividir por zero."
    else:
        return a / b

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção (1-5): ")

        if escolha == '1':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("Resultado:", adicao(num1, num2))

        elif escolha == '2':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("Resultado:", subtracao(num1, num2))

        elif escolha == '3':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("Resultado:", multiplicacao(num1, num2))

        elif escolha == '4':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("Resultado:", divisao(num1, num2))

        elif escolha == '5':
            print("Encerrando...")
            break

        else:
            print("Opção inválida! Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    main()
