#Problem 1:
# 1.1
# Use Tim Sort algorithm (which is the python sorted() function):
#     Uses Insertion Sort for small subarrays (typically < 64 elements)
#     Uses Merge Sort for larger sections
#     Takes advantage of pre-existing order in the data
# Then print out the nth first element in the list

# 1.2
# Tim Sort: O(n log(n))

# 1.3 must submit a .py file
m,n=map(int,input().split())
numbers = sorted([*{int(input()) for _ in range(m)}])
print(f"{n} smallest numbers are: {' '.join(map(str,numbers[:n]))}")
