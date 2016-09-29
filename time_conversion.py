import sys


time = raw_input().strip()
parts = time.split(":")
amOrPm = parts[-1][2]

if amOrPm == "A" and parts[0] == "12":
    parts[0] = "00"
elif amOrPm == "P" and parts[0] != "12":
    part0 = int(parts[0]) + 12
    parts[0] = str(part0) 

parts[-1] = parts[-1][0] + parts[-1][1]

print ":".join(parts)