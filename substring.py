# def get_all_substrings(input_string):
#   length = len(input_string)


#   return [input_string[i:j+1] for i in xrange(length) for j in xrange(i,length)]

# print get_all_substrings('abcde')

# s = "abced"

# length = len(s)
# bank = []
# for i in range(length):
#    for j in range(i,length):
#        if s[i:j+1] not in bank:
#            bank.append(s[i:j+1])
#        if s[i] + s[j+1:length] not in bank:
#            bank.append(s[i] + s[j+1:length])
# bank.sort()

# print(bank)

# def  arrangeCoins(coins):
#     for coin in coins:
#         count = 1
#         num = 0
#         while coin >= count:
#             coin -= count
#             num += 1
#             count += 1
#         print(num)

# print(arrangeCoins([234325435465676785679878,2]))

def powerset(s):
    n = len(s)
    masks = [1<<j for j in xrange(n)]
    for i in xrange(2**n):
        yield [s[j] for j in range(n) if (masks[j] & i)]

bank = []
for elem in powerset([i for i in "abc"]):
    word = "".join(elem)

    if word != "": 
        bank.append("".join(elem))
bank.sort()
print(bank)