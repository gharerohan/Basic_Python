#1️⃣ Reverse a string (without using slicing)

#Problem:
#Write a program to reverse a string without using [::-1].

def reverse_str(s):
    reversed_string = ""
    for char in s:
        reversed_stering = char + reversed_string
    return reversed_string
# Example usage:
input_str = "Hello, World!"
reversed_str = reverse_str(input_str)
print("Original String:", input_str)    
print("Reversed String:", reversed_str)