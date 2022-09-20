import math

def CartesianToPolar():
    r = int(input("Введите значение ρ:"))
    f = int(input("Введите значение φ (радиан):"))

    x = float(r) * (math.cos(int(f)))
    y = float(r) * (math.sin(int(f)))

    return "x = {}, y = {}".format(x, y)

def PolarToCartesian():
    while True:
        try:
            x = float(input("Введите значение X:"))
            y = float(input("Введите значение Y:"))
            break
        except Exception:
            print("Введеные данные не верные!")


    f = math.atan(float(y)/float(x))
    r = math.sqrt(x*x + y*y)

    return "Полярный угол φ = {}(радиан), Полярный радиус r = {}".format(f, r)

choise = input("Выберете преобразование 2D координат:\n 1. полярную в декартовой \n 2. декартовой в полярную\n")

match choise:
    case '1':
        print(CartesianToPolar())
    case '2':
        print(PolarToCartesian())