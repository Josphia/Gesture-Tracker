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


arr = list(input())#[1,2,3,6,4]#input()
res = ""

if len(arr) == 1:
    res = "0"
else:
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            res += str(i)
print(res[-1])
