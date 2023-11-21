data = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 1,
    "h": 2,
    "w": 256,
}

choice = 2
res = list()
for letter in data:
    if choice == data[letter]:
        print(letter)