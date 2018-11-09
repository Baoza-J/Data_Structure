def main():
    a = input('请输入第一个数\n')
    b = input('请输入另一个数\n')

    def yunsuan():
        print('\n现在我将为你们展示"+、-、*、/、//"\n')

        print('a+b ',a+b)
        print('a-b ',a-b)
        print('a*b ',a*b)
        try:
            print('a/b ',a/b)
            print('a//b',a//b)

        except ZeroDivisionError:
            print('除数不能是零')

    def find():
        """
        判断变量a，b的类型是整型还是浮点型
        """
        if '.' in a or '.' in b:
            return True

    try:
        if find():
            a = float(a)
            b = float(b)
            yunsuan()
        else:
            a = int(a)
            b = int(b)
            yunsuan()
    except ValueError:
        print('输入的值有错,你应该输入数字')

if __name__ == '__main__':
    main()
    while 1:
        q = input('是否继续，是的话输入Y，否输入N\n').lower()

        if q == 'y':
            main()
        elif q == 'n':
            break
        else:
            print('请按规范输入')
