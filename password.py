l, u, p, d = 0, 0, 0, 0
s = input("Enter the password ")
for i in s:
    if (i.islower()):
        l += 1
    if (i.isupper()):
        u += 1
    if (i.isdigit()):
        d += 1
    if (i == '@' or i == '$' or i == '#'):
        p += 1
if (l>=1 and u>=1 and p>=1 and d>=1 and len(s)>=8 and len(s)<=12):
	print("Valid Password")
else:
	print("Invalid Password")
if(len(s)>=8 and len(s)<=12):
    print("length of password is in between 8 to 12: ✅")
else:
    print("length of password is in between 8 to 12: ❎")
if(l>=1):
    print("password should contain minimum 1 lowercase alphabet : ✅")
else:
    print("password should contain minimum 1 lowercase alphabet : ❎")
if(u>=1):
    print("password should contain minimum 1 uppercase alphabet : ✅")
else:
    print("password should contain minimum 1 uppercase alphabet : ❎")
if(p>=1):
    print("password should contain minimum 1 special characters out of @ $ # : ✅")
else:
    print("password should contain minimum 1 uppercase alphabet : ❎")
if(d>=1):
    print("password should contain minimum 1 digit: ✅")
else:
    print("password should contain minimum 1 digit: ❎")