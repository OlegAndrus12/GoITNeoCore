
file = open('test.txt', 'w', encoding='utf-8')
file.write('Hello world!\n')
file.write('Hello Ukraine!\n')
file.writelines(['Hi Bob!', 'Hi Dima!', 'Test', 'ups'])
file.close()

file = open('test.txt', 'r', encoding='utf-8')
# size parameter
# result = file.read()
# result = file.readline()
result = file.readlines()
print(result)
file.close()
