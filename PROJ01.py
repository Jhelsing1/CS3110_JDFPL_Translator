import sys
def inputvalidation(char):
    if char.isdigit() == False:
        print("Not a Java decimal floating point literal")
        sys.exit(0)

def a(str1):
    v = str1[len(str1)-1]
    if v == "f" or v == "F" or v == "d" or v == "D":
        return str1[0:len(str1)-1]
    elif v.isdigit() == False:
        print("Not a Java decimal floating point literal")
        sys.exit(0)
    return str1

def b(str1):
    if str1[0] == "-":
        return -1
    else:
        return 1

def construction(num,dec):
    a = dec
    b = 0.0
    for z in num:
        x = num_recog(z)
        b+=x*(10**a)
        a-=1
    b= b /(10**dec)
    return b

def num_recog(num):
    inputvalidation(num)
    switch = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }
    return switch.get(num, "nothing")

def e_var(pwr,sgn):
    a = len(pwr)-1
    b = 1
    for z in pwr:
        x = num_recog(z)
        b+=x*10**a
        a-=1
    if sgn == '-':
        b = b * -1
    return b

def segmenting(str):
    str1 = a(str)
    sg = b(str1)
    if sg == -1:
        str1 = str1[1:len(str1)]
    if str1.find('_') != -1:
        str1 = unscr(str1)
    ind1 = str1.find("e")
    ind2 = str1.find(".")
    mn = 0
    dec = 0
    e = 0
    sign = ""
    tn = 0.0
    tne = 1e0
    if ind1 != -1:
        if ind2 != -1:
            mn = str1[0:ind2] + str1[ind2+1:ind1]
            dec = ind1-ind2-1
            tn = construction(mn,dec)
            e = str1[ind1+1:len(str1)]
            if e[0] == '-':
                sign = '-'
                e = e[1:len(e)]
            elif e[0] == '+':
                e = e[1:len(e)]
            else:
                pass
            tne = tne * tn* sg * 10 **(e_var(e,sign))
            print(tne)
            return tne
        else:
            dec = 0
            mn = str1[0:ind1]
            tn = construction(mn,dec)
            e = str1[ind1+1:len(str1)]
            if e[0] == '-':
                sign = '-'
                e = e[1:len(e)]
            elif e[0] == '+':
                e = e[1:len(e)]
            else:
                pass
            tne = tne * tn* sg * 10 **(e_var(e,sign))
            print(tne)
            return tne
    else:
        if ind2 != -1:
            mn = str1[0:ind2] + str1[ind2+1:len(str1)]
            dec = ind2
            tn = construction(mn,dec)* sg
            print(tn)
            return tn
        else:
            dec = 0
            mn = str1
            tn = construction(mn,dec)* sg
            print(tn)
            return tn

def unscr(str):
    ret = ''
    if str[len(str)-1] == '_':
        print("Not a Java decimal floating point literal")
        sys.exit(0)
    if str[0] == '_':
        print("Not a Java decimal floating point literal")
        sys.exit(0)
    list = str1.split('_')
    list = [x for x in list if x]
    for z in list:
        if z[len(z)-1] == '.':
            print("Not a Java decimal floating point literal")
            sys.exit(0)
        ret+=z
    return ret

x = 'y'

while x == 'y':
    str1 = input("Please enter x:")
    x = segmenting(str1)
    print("functions:")
    print("x + 1")
    x +=1
    print(x)
    print("x / 2")
    x = x /2
    print(x)
    print("x * 3")
    x = x * 3
    print(x)
    x = input("Press \"y\" to continue. ").lower()