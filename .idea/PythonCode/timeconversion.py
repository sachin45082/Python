
def timeConversion(s):
    a = s[len(s)-2:]
    b = s[:2]
    if a =='AM' and b == '12':
        return '00:'+ s[3:-2]
    elif a == 'PM' and b != '12':
        return str(int(b)+12) + s[2:-2]
    else:
        return s[:-2]

if __name__ == '__main__':

    s = input('Please enter the time in hh:mm:ssAM/PM format : ')

    # Check the format of the Time string
    if ((int(s[:2]) >=0 and int(s[:2]) <=12) and
        (s[2] == ':') and
        (int(s[3:5]) >=0 and int(s[3:5]) <=60) and
        (s[5] == ':') and
        (int(s[6:8]) >=0 and int(s[6:8]) <=60) and
        (s[8:] == 'AM' or s[8:] == 'PM')):
                 result = timeConversion(s)
                 print(result)
    else:
        print('The format is not correct. Please enter the time in hh:mm:ssAM/PM format')