# 1.append(W) - Append string W to the end of .
# 2.delete(k) - Delete the last k characters of .
# 3.print(k) - Print the kth character of .
# 4.undo() - Undo the last (not previously undone) operation of type 1 or 2, reverting S to the state it was in prior to that operation.

def process_query(S, option, entry=None):
    if option == 1:
        S = S + entry
    elif option == 2:
        temp = ""
        for i in range(len(S) - int(entry)):
            temp = temp + S[i]
        S = temp
        print S
    elif option == 3:
        print S[int(entry) - 1]
    return S

S = ""
prior = [""]
n = int(raw_input())

for i in range(n):
    query = str(raw_input())
    arr = query.split(" ")
    if len(arr) > 1:
        S = process_query(S, int(arr[0]), arr[1])
        if int(arr[0]) != 3:
            prior.append(S)
    else:
        del prior[-1]
        S = prior[-1]
    print prior
    print "S: " + S

