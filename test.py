# s = input()

# res = 0 

# for i in range(len(s)):
#     toCheck = ""
#     for j in range(i, len(s)):
#         if s[j] not in toCheck:
#             toCheck+= s[j]
#         else:
#             break

#     if len(toCheck)>res:
#         res = len(toCheck)

# print(res)


s = "abcabcbb"#input()

count = 0 

for i in range(0, len(s)):
    toCheck = ""
    for j in range(i, len(s)):
        if s[j] not in toCheck:
            toCheck += s[j]
        else:
            break
        if len(toCheck)>count:
            count = len(toCheck)
    
print(count)