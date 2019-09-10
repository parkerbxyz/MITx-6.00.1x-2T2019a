valid_vowels = ['a', 'e', 'i', 'o', 'u']

vowels_found = 0
for c in s:
    if c in valid_vowels:
        vowels_found += 1

print("Number of vowels: {}".format(vowels_found))
