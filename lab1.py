from math import sqrt


def calculate(a: float, b: float, c: float) -> str:
    if a == 0:
        if b == 0:
            if c == 0:
                return "X - любое число"
            else:
                return "Решений нет"
        else:
            x = - c / b
            return f"x = {x}"
    else:
        D = b**2 - 4 * a * c

        if D == 0:
            x = - b / (2 * a)
            return f"x = {x}"

        elif D > 0:
            x1 = (-b + sqrt(D)) / (2 * a)
            x2 = (-b - sqrt(D)) / (2 * a)
            return f"x1 = {x1}\nx2 = {x2}"

        else:
            return "Решений нет"


def main() -> None:
    while True:
        try:
            a = float(input("Введите a: "))
            b = float(input("Введите b: "))
            c = float(input("Введите c: "))
            print(calculate(a, b, c))
            break
        except:
            print("Ошибка. Неверный формат аргументов. Введите числа с разделителем в виде точки")


if __name__ == "__main__":
    main()
