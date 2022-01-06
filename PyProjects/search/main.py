
from bsearch import bsearch


list = [100,1,3,5,6,7,8,9,10,33,452,345,4,11,99,1,3,5]

#to remove duplicates converts into set.
myset = set(list)

#we are sorting it using sorted.
data = sorted(myset)

print(f"list is {data}")

term = int(input("Enter the search term :"))

sea = bsearch(data,term)

index = sea.mysearch()

print(f"present in the position {index}")