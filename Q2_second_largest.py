#2️⃣ Find the second largest number in a list

#Problem:
#Given: arr = [12, 35, 1, 10, 34, 1]
#Print the second largest unique number.

def find_second_largest(arr):
    first=second = float('-inf')
    for number in arr:
        if number > first:
            second = first
            first= number
        elif first > number > second:
            second = number
    return second if second != float('-inf') else None
# Example usage:
arr = [12, 35, 1, 10, 34, 1]
second_largest = find_second_largest(arr)
print("The second largest number is:", second_largest)

