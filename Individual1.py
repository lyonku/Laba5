if __name__ == '__main__':
    words = input("Введите предложение: ")
    a = 1
    for i in words:
        if a % 3 == 0:
            print(i)
        a = a + 1