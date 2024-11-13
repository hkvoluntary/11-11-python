# Print each item in a list
fruits = ["apple", "banana", "cherry", "pear"]



for i in range(-1, -len(fruits)-1,-1):
    print(fruits[i])

count = len(fruits)
while (count > 0):
    print(fruits[count-1])
    count = count - 1

""""
print(type(fruit))
print(type(i))

# Print index and value for each item in the list
fruits = ["apple", "banana", "cherry"]
for index, f in enumerate(fruits):
    print(index, f)

print(type(f))
print(type(index))

"""