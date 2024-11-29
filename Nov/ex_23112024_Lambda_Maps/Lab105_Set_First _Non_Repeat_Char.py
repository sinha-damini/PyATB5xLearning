# Find the first non-repeating character in a string using sets.
# swiss -> s -x , w - Anwser

def fir_non_repeat_char(string):
    for char in string:
        if string.count(char) == 1:
            return char

    return None

print(fir_non_repeat_char("swiss"))
print(fir_non_repeat_char("swwiiss"))







