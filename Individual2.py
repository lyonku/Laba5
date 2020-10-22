if __name__ == '__main__':
    words = input("Введите предложение: ")
    a = len(words)
    s = 2
    while s <= a:
        words = words.replace(words[s], 'а')
        s += 3
    print(words)
