"""
逻辑运算符
"""
def main():
    print()
    print('展示逻辑运算符')
    try:
        a = int(input('Enter a\n'))
        b = int(input('Enter b\n'))
    except valueError:
        a = input('Enter a \n')
        b = input('Enter b \n')
    print()
    print('a and b', a and b)
    print('not(a and b)', not(a and b))
    print('a or b', a or b)
    print('not(a or b)', not(a or b))
    print()

if __name__ == '__main__':
    main()
    while 1:
        r = input('继续按Y,退出按N\n')
        r = r.lower()
        if r == 'y':
            main()
        elif r == 'n':
            break
        else:
            print('try again\n')
