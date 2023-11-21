
l1 = set(["Red", "Green", "Black", "White"])
l2 = set(["Red", "White"])

#res = l1.intersection(l2)
# | = pipe
#  & - перетин, | об'єднання, ^ симетрична різниця, - різниця
res = l2.issubset(l1)




print(res)
