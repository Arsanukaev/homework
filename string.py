while True:
    def line (str1, str2):
        if type(str1) is not str or type(str2) is not str:
            return 0
        elif str1 == str2:
            return 1
        elif str1 != str2 and str2 == 'learn':
            return 3
        elif len(str1) > len(str2):
            return 2
    print ("Введите а:")
    a = input()
    print ("Введите б:")  
    b = input()
    c = line(a, b)

    print (c)
