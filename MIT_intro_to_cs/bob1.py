s = 'azcbobobegghakl'
b = 0
if 'bob' in s:
    print('\'bob\' in string \'s\'')
    i = 0
    for char in s:
        print('char ' + str(i) + ' in string \'s\': ' + char)
        if char == 'b':
            i += 1
            for char in s[i]:
                print('Found letter \'b\', checking for \'o\'')
                if char == 'o':
                    i += 1
                    for char in s[i]:
                        print('Found letter \'o\', checking for last \'b\'')
                        if char == 'b':
                            b += 1
                            i += 1
                            for char in s[i]:
                                print('Found last \'b\', added one to the bob tally, checking if followed by another \'o\'')
                                if char == 'o':
                                    i += 1
                                    for char in s[i]:
                                        print('Found another \'o\', checking for \'b\'')
                                        if char == 'b':
                                            b += 1
                                            i += 1
                                            print('Found \'b\', added one to the bob tally, that makes two, checking if followed by another \'o\'')
                                        else:
                                            i += 1
                        else:
                            i += 1
                else:
                    i += 1
        else:
            i += 1
print('Number of times bob occurs is: ' + str(b))