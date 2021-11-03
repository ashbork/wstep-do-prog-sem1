nazwiska = ["Kowalski", "Nowak", "Adamski", "Bond", "Jasiński"]
# list comprehension filtrujące elementy po pierwszym znaku
print([lname for lname in nazwiska if lname[0] >= "K"])
# ekwiwalentne:
# result = []
# for lname in nazwiska:
#     if lname[0] >= "K":
#         result.append(lname)
# print(result)

# list comprehension filtrujące elementy po długości, po czym posortowane funkcją sorted()
print(sorted([lname for lname in nazwiska if len(lname) > 5]))
# ekwiwalentne:
# result = []
# for lname in nazwiska:
#     if len(lname) > 5:
#         result.append(lname)
# result.sort()
# print(result)