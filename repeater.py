def repeater(string):
    for x in range(0, len(string) - 1):
        if string[x] == string[x + 1]:
            print(string[x], x)

repeater('test')
repeater('congee')
repeater('little')