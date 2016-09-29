def  stringSimilarity(inputs):
    from itertools import izip
    res = []
    for inpt in inputs:
        #inputLen = 0
        sum = 0
        compareStrings = [inpt[i:] for i in range(len(inpt))]
        k = 0
        #print(compareStrings)
        while k < len(inpt):
            for i, j in izip(inpt, compareStrings[k]):
                if i == j:
                    sum += 1
                    print("i, j: " + i +", "+j)
                else:
                    break
            k += 1
        
        res.append(sum)
    return res

# def get_similarity(a, suffix):
#     from itertools import izip
#     score = 0
#     for a, b in izip(a, suffix):
#         print("a, b: " + a + ", " + b)
#         if a != b:
#             break
#         score += 1
#     return score

# def stringSimilarity(a):
#     # makes all possible suffixes for a string:
#     # ababaaa becomes ababaaa, babaaa, abaaa, baaa, aaa, aa, a
#     # and then counts how many prefixes between the suffix and the string are shared
#     # abaaaa shares 3 prefixes with ababaaa
#     # and sums up the shared prefixes
#     answer = 0
#     i = 0
#     while i < len(a):
#         suffix = a[i:]
#         answer += get_similarity(a, suffix)
#         i += 1
#     return answer

L = stringSimilarity(["ababaa", "aa"])
#L = ["looking", "aa"]
for i in range(len(L)):
    print(L[i])