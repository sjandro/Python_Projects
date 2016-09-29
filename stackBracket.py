import sys

f = open("brackets.txt", "r")
w = open("output.txt", "w")
lines = f.readlines()
f.close()
t = int(lines[0])
for a0 in xrange(1,t+1):
    s = lines[a0].strip()
    pattern = []
    for c in s:
        if c in ["{","[","("]:
            pattern.append(c)
        elif len(pattern) != 0:
            if pattern[-1] == "(" and c == ")":
                del pattern[-1]
            elif pattern[-1] == "{" and c == "}":
                del pattern[-1]
            elif pattern[-1] == "[" and c == "]":
                del pattern[-1]
            else:
                break
    if len(pattern) == 0:
        w.write("YES\n")
    else:
        w.write("NO\n")
w.close()

from itertools import izip

f1 = open("expected_answer.txt", "r")
f2 = open("output.txt", "r")
out = open("diff.txt", "w")
count = 1
for i, j in izip(f1.readlines(), f2.readlines()):
    if i.strip() != j.strip():
        out.write(str(count) + ": " + i.strip() + " , " + j.strip() + "\n")
    count += 1
f1.close()
f2.close()
out.close()
