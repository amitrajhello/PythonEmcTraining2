# Tuples are also called read-only lists , we can not change the values inside the tuples
items = (2.2, 'kim', 'rose', 'wall', 'eva', 'oliver', 3.1, 3)

#items[-2} = 1.3 #immutable
print(items)
print(type(items))
print(len(items))
print()
print(items[-3])
print(items[-3:])
print(items[:3])
print()

for item in items[:3]:
    print(item)



