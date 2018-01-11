# coding=utf-8
import itertools
charset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0','1', '2', '3', '4', '5', '6', '7', '8', '9','!','@','#','$','%','&','*',',','.']
length = input('请输入输入的位数(不少于8位):')
maxLength = input('请输入最大的位数(不多于15位):')
if int(length) < 8:
    print('输入错误')
    exit()
if int(maxLength) > 15:
    print('输出错误')
    exit()
count = int(length)
while count < maxLength:
    string = ''
    for c in  charset:
       string = string + c
    r = itertools.product(string, repeat=count)
    fileName = '%s.txt' % str(count)
    dic = open(fileName, 'w')
    for i in r:
         print '%s' % ''.join(i)
         dic.write(''.join(i))
         dic.write("".join("\n"))
    dic.close()
    count = count + 1

