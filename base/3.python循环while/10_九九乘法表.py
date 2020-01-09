# 九九乘法表
row = 0
while row < 9:
    row += 1
    col = 0

    while col < row:
        col += 1
        # end = ""，表示输出结束后，不换行
        # "\t" 可以在控制台输出一个制表符，协助在输出文本时对齐
        print('%d * %d = %d' % (col, row, row*col), end='\t')
    print('')
