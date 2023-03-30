import sys
def calculadora(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        print("Operador inválido")
        sys.exit(1)

num1 = float(input("Digite o primeiro número:   "))
op = input("Digite o operador(+, -, *, /): ")
num2 = float(input("Digite o segundo número:   "))

resultado = calculadora(num1, num2, op)
print(f" o resultado é: {resultado}")