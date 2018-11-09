"""
    通过比较运算符比较两次输入的内容
"""
def main():
    print()
    print('展示比较运算符')
    a = input('Enter a\n')
    b = input('Enter b\n')
    print()
    print('a < b', a < b)
    print('a <= b', a <= b)
    print('a > b', a > b)
    print('a >= b', a >= b)
    print('a == b', a == b)
    print('a != b', a != b)
    print('a is b', a is b)
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
