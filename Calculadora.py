import math

class Calculator:
    def __init__(self):
        pass
    def sum1(self, number1:int, number2:int)->int:
        return number1 + number2
    def subtraction(self, number1:int, number2:int)->int:
        return number1 - number2
    def multiplication(self, number1:int, number2:int)->int:
        return number1 * number2
    def division(self, number1:int, number2:int)->float:
        if number1 == 0 or number2 == 0:
            return "Error"
        return number1 / number2
    def percentage(self, value:int, percentage:float)->float:
        return (value * percentage) / 100
    def squareroot(self, number1:int):
        return math.sqrt(number1)
    def potentiation(self, base:int, exponent:int)->int:
        return base ** exponent
number1 = int(input('Digite um número: '))
selector = str(input('Selecione o operador (+, -, *, /, %, raiz, ^): '))

calc = Calculator()
 
if selector == '+':
    number2 = int(input('Digite o segundo número: '))
    print(calc.sum1(number1, number2))

elif selector == '-':
    number2 = int(input('Digite o segundo número: ')) 
    print(calc.subtraction(number1, number2))

elif selector == '*':
    number2 = int(input('Digite o segundo número: ')) 
    print(calc.multiplication(number1, number2))

elif selector == '/':
    number2 = int(input('Digite o segundo número: ')) 
    print(calc.division(number1, number2))

elif selector == '%':
    number2 = int(input('Digite o segundo número: ')) 
    print(calc.percentage(number1, number2))

elif selector == 'raiz': 
    print(calc.squareroot(number1))

elif selector == '^':
    number2 = int(input('Digite o segundo número: ')) 
    print(calc.potentiation(number1, number2))

else:
    print("Operação inválida!")