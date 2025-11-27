#Linear Search Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [5, 3, 7, 9, 2, 8]
target = 9

result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")
