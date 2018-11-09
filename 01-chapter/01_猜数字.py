import random

def main():
    smaller = int(input('请输入比较小的那一个数'))
    larger = int(input('请输入比较大的那一个数'))

    the_number = random.randint(smaller, larger)
    count = 0
    while 1: #词法元素
        count += 1 # 赋值语句等价于 count = count+1
        answer = int(input('请输入你的答案'))
        if answer < the_number:
            print('太小了')
        elif answer > the_number:
            print('太大了')
        else :
            print('你得到这个数用了"%d"次' % count)
            break
if __name__ == '__main__':
    main()
