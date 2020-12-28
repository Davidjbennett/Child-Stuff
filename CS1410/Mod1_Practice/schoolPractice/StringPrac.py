str = "Practicing some good ole code today"
strStrip = "\t im gonna strip the\t heck outta this string \t\n" #\n is a newline \t is a tab

print(strStrip)
print(strStrip.rstrip())
print(strStrip.lstrip())
print(strStrip.strip())


strArr1 = str.split("o")
print(strArr1)

strArr = str.split("oo")
print(strArr)

print('!'.join(strArr))

str2 = '$'.join(strArr1)
print(str2)

print(str.find("o"))
print(str.rfind("o"))
print(str.find("some"))

