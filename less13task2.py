def seq_generator(sequence):
    while True:
        for number in sequence:
            yield number


def main():
    try:
        count = int(input("Введите количество чисел для вывода: "))
        if count <= 0:
            print("число должно быть больше 0")
            return

        seq = [1, 2, 3]
        generator = seq_generator(seq)

        print("Циклическая последовательность чисел:")
        for _ in range(count):
            print(next(generator), end=" ")
    except ValueError:
        print("введено не целое число")


if __name__ == "__main__":
    main()