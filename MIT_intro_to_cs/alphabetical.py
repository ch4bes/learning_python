#s = 'zxyabcddcb'
s = 'azcbobobegghaklabcdefg'
i = 0 # iterations
l = 0 # length of longestString
tempLongString = ''
longestString = ''
#print(len(s))
print(s)
for char in s:
    #print(str(i))
    t = 0 # tempValue
    print('char ' + str(i) + ' is: ' + char)
    while(i+1 < len(s) and s[i] <= s[i+1]):
        t += 1
        tempLongString = tempLongString + char
        print(s[i] + ' <= ' + s[i+1] + ' ' + char + ': length is: ' + str(t))
        #break
        i += 1
        if(t >= l): ##and #tempLongString > longestString):
            l = t
            longestString = tempLongString
            print('tempValue: ' + str(t) + ', longestString: ' + str(l))
            #break
    #else:
        #break
    i += 1
print('Done. Longest alphabetical string is: ' + str(t))
