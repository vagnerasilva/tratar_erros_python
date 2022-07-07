try:
    num1 = 3
    num2 = 0
    response = num1 / num2
    print(response)
except ZeroDivisionError:
    print("Erro de divisao de zero ")
except Exception as exception:
    print(exception)
    print(" ocorreu um erro ")
finally:
    print("encerramento ")
