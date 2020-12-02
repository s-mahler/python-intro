def reverse_string(string):
    print(string [::-1])

def reverse_string_slice(string):
    x = slice(len(string), 0, -1)
    print(string[x] + string[0])

reverse_string('yellow')
reverse_string_slice('holding')