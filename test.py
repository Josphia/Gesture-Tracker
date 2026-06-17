s = "babad"

for i in range(0, len(s)):
    toCheck = ""
    for j in range(i, len(s)):
        toCheck += s[j]
        print(toCheck)
        # while(len(toCheck)>1):
        #     if toCheck == toCheck[:-1]:
        #         print(toCheck)
        #         break
