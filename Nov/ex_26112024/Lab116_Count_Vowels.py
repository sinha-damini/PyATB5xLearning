input_string = input("Enter input\n")
# vowel = a,e, i,o,u.


vowels = "aeiou"
vowels_count = 0

result = dict()

for char in input_string:
    if char in vowels:
        vowels_count = vowels_count + 1
        result[char] = result.get(char, 0)+1

print(vowels_count)
print(result)