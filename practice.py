# Missing number
def getMissingNum(A):
    n = len(A)
    total = (n + 1) * (n + 2) / 2
    sum_A = sum(A)
    return total - sum_A


arr1 = [1, 3, 4, 5, 6]
miss_no = getMissingNum(arr1)
print(int(miss_no))

#
arr2 = [1, 2, 3, 4, 5, 6, 7, 9]
missing_num = []
for num in range(arr2[0], arr2[-1] + 1):
    if num not in arr2:
        missing_num.append(num)
print(missing_num)


# Min and Max values
def minMax():
    num = [2, 3, 4, 1, 5, 6, 10, 9]
    min_num = min(num)
    max_num = max(num)
    return min_num, max_num


print(minMax())

# Remove Duplicates
arr5 = [1, 2, 1, 2, 5, 6, 4, 9, 3, 2, 8]
dup = []
for num in arr5:
    if num not in dup:
        dup.append(num)
print(dup)


# Find Duplicates
def fun5(A):
    duplicates = [num for num in numbers if numbers.count(num) > 1]
    res = list(set(duplicates))
    print(res)

numbers = [0, 1, 2, 1, 2, 5, 6, 4, 9, 3, 2, 8, 0, 1]
fun5(numbers)

# Number of occurrences:
n = [1,2,3,1,2,3,4,5,6,7,8,9]
p = n.count(1)
print(p)

np = [1,-1,-5,6,5,9]
np.sort()
print(np)