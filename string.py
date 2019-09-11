def line (str1, str2):
    if type(str1) is not str or type(str2) is not str:
        return 0
    elif str1 == str2:
        return 1
    elif str1 != str2 and str2 == 'learn':
        return 3
    elif str1 != str2 and str1 > str2:
        return 2
    
d = line(1, "ff")
a = line("read", 'read')
b = line("read1", 'read')
c = line("read1", 'learn')

print (a)
print (b)
print (c)
print (d)