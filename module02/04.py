
a = 1
b = 43

l = [100, 43, 1, 142, 21]

max_index = 0
maximum = l[0]

for i in range(len(l)):
    if l[i] > maximum:
        maximum = l[i]
        max_index = i

print(maximum)
print(max_index)
