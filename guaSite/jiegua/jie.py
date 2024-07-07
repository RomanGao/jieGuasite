num2Char = ['-', '初', '二', '三', '四', '五', '上']


def get6or9(gx, nd):
    index = int(nd) - 1
    if gx[index] == '0':
        return "六"
    else:
        return "九"


def printYaoResult(gx, nd):
    yy = get6or9(gx, nd)  # 6或者9
    if int(nd) == 1 or int(nd) == 6:
        print("使用[", num2Char[int(nd)], yy, '爻]', '爻辞推之')
        return "".join(["使用[", num2Char[int(nd)], yy, '爻]', '爻辞推之'])
    else:
        print("使用[", yy, num2Char[int(nd)], '爻]', '爻辞推之')
        return "".join(["使用[", yy, num2Char[int(nd)], '爻]', '爻辞推之'])


def get_yao(gx, nd):
    if len(nd) == 1:
        if int(nd) == 0:
            print("本卦无动爻,使用本卦卦辞断之")
            return "本卦无动爻,使用本卦卦辞断之"
        else:
            return printYaoResult(gx, nd)
    # 两个动爻
    elif len(nd) == 2:
        if (gx[int(nd[0]) - 1] == '0' and gx[int(nd[1]) - 1] == '0') \
                or (gx[int(nd[0]) - 1] == '1' and gx[int(nd[1]) - 1] == '1'):
            return printYaoResult(gx, nd[1])
        elif gx[int(nd[0]) - 1] == '0':
            return printYaoResult(gx, nd[0])
        else:
            return printYaoResult(gx, nd[1])
    elif len(nd) == 3:
        return printYaoResult(gx, nd[1])
    elif len(nd) == 4:  # 最下面的非动
        temp = '123456'
        for i in nd:
            temp = temp.replace(i, '')
        return printYaoResult(gx, temp[0])
    elif len(nd) == 5:  # 取非动
        temp = '123456'
        for i in nd:
            temp = temp.replace(i, '')
        return printYaoResult(gx, temp)
    else:
        if '1' not in gx:  # 六阴爻
            print('坤卦，‘用六’断之')
            return '坤卦，‘用六’断之'
        elif '0' not in gx:  # 六阳爻
            print('乾卦，‘用九’断之')
            return '乾卦，‘用九’断之'
        else:
            print('按八宫卦的前一个卦辞断之')
            return '按八宫卦的前一个卦辞断之'