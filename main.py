import re


sign = {"-", "+", "/", "*"}
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

def calc(count=0):

    result = re.split(r'[\+\-\/\*]', x)

    for i in result:
        if int(i) in numbers :
            continue
        else:
            raise ValueError("Значения не соответсвуют задаче")

    for j in x:
        if j in sign:
            count += 1

    if count < 1:
        raise ValueError("Строка не является математической операцией")
    elif count > 1:
        raise ValueError(
            "Формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")
    else:
        if type(eval(x)) == int or float:
            print("%.0f" % eval(x))
        else:
            raise ValueError("Неправильная запись операции")


if __name__ == "__main__":
    while True:
        x = input("Введите пример для вычисления: ")
        calc()