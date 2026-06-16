s = "abcabcbb"

toCheck = s[0]

for i in range(1, len(s)):
    if toCheck+s[i] in s:
        print(toCheck+s[i])
        toCheck = toCheck+s[i]
        

print(toCheck)
