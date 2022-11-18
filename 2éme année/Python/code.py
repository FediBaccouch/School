"""
ch = str(input("donner ch: "))

l = str(len(ch))
p = ch.find(" ") + 1
code = "T" + l + ch[0].upper() + ch[p].upper()
print(code)
"""
"""
ch = str(input("donner ch: "))

l = str(len(ch))
p = ch.find(" ") + 1
premiere = ch[:1]
deuxieme = ch[p:p + 1]
code = "T" + l + premiere.upper() + deuxieme.upper()
print(code)
"""
ch = str(input("donner ch:"))

l = str(len(ch))
p = ch.find(" ")
ch1 = ch[:p]
ch2 = ch[p+1:]
code = "T" + l + ch1[0].upper() + ch2[0].upper()
print(code) 