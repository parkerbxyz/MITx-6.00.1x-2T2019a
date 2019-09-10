bobs_found = 0
start_index = 0

while start_index < len(s):
    # the index at which 'bob' is found in the given string
    bob_index = s.find('bob', start_index)

    # if 'bob' is found
    if bob_index != -1:
        bobs_found += 1
        # change start_index to the position where this 'bob' was found + 1
        start_index = bob_index + 1
    else:
        # stop looking for 'bob'
        break

print("Number of times bob occurs is: {}".format(bobs_found))
