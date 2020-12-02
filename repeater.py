def repeater(string):
    for x in range(0, len(string) - 1):
        if string[x] == string[x + 1]:
            print(string[x + 1], x + 1)
            break
    else: 
        print('no repeating characters')

repeater('test')
repeater('congee')
repeater('little')
repeater('mississippi')

def number_repeater(array):
    count = 0
    most = 0
    for x in range(0, len(array) - 1):
        if array[x] == 1:
            count += 1
            if count > most:
                most = count
        elif array[x] == 0:
            count = 0
    else:
        print(most)

test = [0,1,1,1,1,0,1]
number_repeater(test)
number_repeater([1,1,0])
