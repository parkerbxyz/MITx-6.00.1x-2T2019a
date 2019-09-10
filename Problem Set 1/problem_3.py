substring = s[0]  # the first letter in the given string
substring_list = []

# iterate over each letter in the given string starting with the second letter
for letter in s[1:]:
    previous_letter = substring[-1]  # the last letter of the substring

    # if the previous letter comes before this letter in the alphabet
    if previous_letter <= letter:
        # append this letter to the substring
        substring += letter
    else:
        # append substring to the list
        substring_list.append(substring)
        # replace substring with the letter
        substring = letter

substring_list.append(substring)  # append substring to the list
longest_substring = max(substring_list, key=len)

print("Longest substring in alphabetical order is: {}"
      .format(longest_substring))
