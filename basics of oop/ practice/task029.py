# NORMAL WAY

# doubles = []

# for i in range(1, 11):
#     doubles.append(i * 2)

# print(doubles)

# LIST COMPREHENSION

# doubles = [x * 2 for x in range(1, 11)]

# triples = [y * 3 for y in range(1, 11)]

# square = [b ** 2 for b in range(1, 11)]

# print(doubles)
# print(triples)
# print(square)


# fruits = ["apples", "orange", "banana", "coconut"]

# makes all fruits uppercase

# fruits = [fruit.upper() for fruit in fruits]
# print(fruits) 

# fruits = [fruit.upper() for fruit in ["apples", "orange", "banana", "coconut"]] we can also write it this way


# fruits = ["apples", "orange", "banana", "coconut"]
#prints all fruits first characters 

# fruit_chars = [fruit[0] for fruit in fruits]
# print(fruit_chars)


# if conditions in list comprehension

# numbers = [1, -2, 3, -4, 5, -6, 8, -7]

# if numbers from this list are greater or same as zero it will return those numbers

# positives = [num for num in numbers if num >= 0]
# print(positives)
# now negatives
# negatives = [num1 for num1 in numbers if num1 < 0]
# print(negatives)

# now even numbers
# even = [num for num in numbers if num % 2 == 0]
# print(even)

#now odd numbers
# odd = [num for num in numbers if num % 2 != 0]
# print(odd)

grades = [85, 42, 79, 90, 56, 61, 20]

passing = [grade for grade in grades if grade >= 70]

print(passing)