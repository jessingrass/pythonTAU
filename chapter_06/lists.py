fruits = ["peaches", "apples", "pears", "apples", "apples"]
years = [3, "1998", 2.5, 987, "1994"]

print("apple" in fruits)
print("apples" in fruits)

print(fruits, years)

fruits.append("oranges")
print(fruits)

fruits.extend(years)
print(fruits)

fruits.remove("oranges")
print(fruits)

fruits.pop(0)
print(fruits)

fruits.pop(-1)
print(fruits)

fruits.sort()
print(fruits)

numbers = [5, 1928, 4, 17, 68, 73.76, 20.458]
numbers.sort()
print(numbers)

print(fruits.count("apples"))
print(fruits.count("apple"))

print(fruits.index("apples"))
