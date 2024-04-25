fname = str(input("Enter First Name: "))
countfname = int(0)
for letter in fname:
    countfname += 1
print(countfname)

sname = str(input("Enter Surname: "))
countsname = int(0)
for letter in sname:
    countsname += 1
print(countsname)

print(fname, sname)
print(countfname+countsname+1)
