
def fibonacci_number_generator(numb):
    a, b = 0, 1
    for _ in range(numb):
        yield a
        a, b = b, a + b

def main():
    try:
        numb = int(input("Задайте номер числа Фибоначи, до которого нужно выводить : "))
        if numb <= 0:
            print("число должно быть больше 0.")
            return

        print(f"Последовательность чисел Фибоначчи до {numb}-го числа:")
        for number in fibonacci_number_generator(numb):
            print(number, end=" ")
    except ValueError:
        print("Пожалуйста, введите целое число.")


if __name__ == "__main__":
    main()

