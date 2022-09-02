
with open("file1.txt") as file:
  numbers = file.readlines()
  numbers1 = [int(num[:-1]) for num in numbers]
print(numbers1)

with open("file2.txt") as file:
  numbers = file.readlines()
  numbers2 = [int(num[:-1]) for num in numbers]
print(numbers2)

result = [number for number in numbers1 if number in numbers2]


# Write your code above 👆

print(result)


