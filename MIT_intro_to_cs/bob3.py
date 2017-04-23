s = 'jbbobobbobsbbbooboboboobooobbobobooowobxdsbobfodcodfce'
b = 0
if 'bob' in s:
    i = 0
    for char in s:
        # print('char ' + str(i) + ' is: ' + char)
        while char == 'b':
            # print('found b')
            if(i+2 < len(s)):
                for char2 in s[i+1]:
                    while char2 == 'o':
                        # print('found o')
                        for char3 in s[i+2]:
                            while char3 == 'b':
                                # print('ok, bob')
                                b += 1
                                break
                        break
            break
                        
        i += 1
print('Number of times bob occurs is: ' + str(b))