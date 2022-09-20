import math


def CartesianToSpherical(): # от декартовых к сферическим
    x = float(input("Введите значение x: "))
    y = float(input("Введите значение y: "))
    z = float(input("Введите значение z: "))

    r = math.sqrt(x**2 + y**2 + z**2)
    fi = math.degrees(math.atan2(y, x))
    teta =  math.degrees(math.atan(math.sqrt(x**2 + y**2) / z))
    return "Радиус (ρ) = {}\nАзимут (φ) = {}\nПолярный угол (θ) = {}".format(round(r, 2), round(fi, 2), round(teta, 2))


def SphericalToCartesian(): # от сферических к декартовым
    ro = float(input("Введите значение Ro:"))
    fi = float(input("Введите значение Fi (градусы):"))
    teta = float(input("Введите значение Teta (градусы):"))

    x = ro * math.sin(math.radians(teta)) * math.cos(math.radians(fi))
    y = ro * math.sin(math.radians(teta)) * math.sin(math.radians(fi))
    z = ro * math.cos(math.radians(teta))

    return "x = {}\ny = {}\nz = {}".format(round(x, 2), round(y, 2), round(z, 2))


def main():
    choise = input("Выберете преобразование 3D координат:\n 1. от декартовых к сферическим \n 2. от сферических к декартовым\n")

    if choise == '1':
        print(CartesianToSpherical())
    elif choise == '2':
        print(SphericalToCartesian())
    else:
        print("Вариант " + choise + " не существует!")
if __name__ == "__main__":
    main()