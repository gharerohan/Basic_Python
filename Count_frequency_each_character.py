#3️⃣ Count frequency of each character

#Problem:
#Input: "mississippi"
#Output: {'m': 1, 'i': 4, 's': 4, 'p': 2}
def count_character_frequency(s):
    frequency ={}
    for char in s:
        if char in frequency:
            frequency[char] +=1
        else:
            frequency[char] =1 
    return frequency 
# Example usage:
input_str = "mississippi"
char_frequency = count_character_frequency(input_str)
print("Character Frequency:", char_frequency)