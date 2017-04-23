s = 'azcbobobegghakl'
b = 0
if 'bob' in s:
    print('\'bob\' in string \'s\'')
    i = 0
    for char in s:
        print('char ' + str(i) + ' in string \'s\': ' + char)
        while char == 'b':
            print('found b')
            for char in s[i+1]:
                while char == 'o':
                    print('found o')
                    for char in s[i+1]:
                        if char == 'b':
                            print('ok, bob')
                            b += 1
                            i += 1
                        else:
                            i += 1
        i += 1
print('Number of times bob occurs is: ' + str(b))