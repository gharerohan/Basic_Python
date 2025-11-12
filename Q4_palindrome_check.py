#4️⃣ Check if a string is palindrome

#Problem:
#Write a program to check if a string reads the same forward and backward.
def is_palindrome(s):
    left,right = 0, len(s) -1
    while left < right:
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
    return True
# Example usage:
input_str = "racecar"
if is_palindrome(input_str):
    print(f'"{input_str}" is a palindrome.')
else:
    print(f'"{input_str}" is not a palindrome.')
     