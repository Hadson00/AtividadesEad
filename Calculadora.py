import math

class Calculator:
    def __init__(self):
        pass
    def sum(self, number1, number2):
        return number1 + number2
    def subtraction(self, number1, number2):
        return number1 - number2
    def multiplication(self, number1, number2):
        return number1 * number2
    def division(self, number1, number2):
        if number2 == 0:
            return "Error"
        return number1 / number2
    def percentage(self, value, percentage):
        return (value * percentage) / 100
    def squareroot(self, number1):
        return math.sqrt(number1)
    def potentiation(self, base, exponent):
        return base ** exponent
number1 = int(input('Digite um número: '))
selector = str(input('Selecione o operador: '))

x = Calculator()
 
if selector == '+':
    number2 = int(input('Digite o segundo número: '))
    result = x.sum(number1, number2)
    print(result)

elif selector == '-':
    number2 = int(input('Digite o segundo número: '))
    result = x.subtraction(number1, number2)
    print(result)

elif selector == '*':
    number2 = int(input('Digite o segundo número: '))
    result = x.multiplication(number1, number2)
    print(result)

elif selector == '/':
    number2 = int(input('Digite o segundo número: '))
    result = x.division(number1, number2)
    print(result)

elif selector == '%':
    number2 = int(input('Digite o segundo número: '))
    result = x.percentage(number1, number2)
    print(result)

elif selector == 'raiz':
    result = x.squareroot(number1)
    print(result)

elif selector == '^':
    number2 = int(input('Digite o segundo número: '))
    result = x.potentiation(number1, number2)
    print(result)

else:
    print("Operação inválida!")
