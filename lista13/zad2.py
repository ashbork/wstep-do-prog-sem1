divby_three_or_five = lambda a : True if (a % 3 == 0 or a % 5 == 0) and a != 0 else False

result = []
for num in filter(divby_three_or_five, range(50)):
    result.append(num)
print(result)

# alternatywnie (zwięźlej i czytelniej):
# [num for num in range(50) if num % 3 == 0 and num % 5 == 0]
