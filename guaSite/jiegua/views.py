from django.shortcuts import render
from .gua import Gua
from .jie import *
# Create your views here.
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    # order_by参数用_可以作为提示
    #output = ", ".join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

    return render(request, "index.html")

def detail(request):
    gx = request.POST.get('guaNo')
    nd = request.POST.get('dongNo')

    if len(nd) == 0:
        nd = '0'
    if (len(gx) != 6):
        context = "输入卦相的长度错误，请重新输入！"
        print(context)
        return render(request, "detail.html", {"context": context})
    if (len(gx) > 6):
        context = "输入动爻的长度错误，请重新输入！"
        print(context)
        return render(request, "detail.html", {"context": context})
    for i in gx:
        if i not in ['0', '1']:
            context = "卦相输入错误，请重新输入！"
            print(context)
            return render(request, "detail.html", {"context": context})
    for i in nd:
        if int(i) > 6 or int(i) < 0:
            context = "动爻输入错误，请重新输入！"
            print(context)
            return render(request, "detail.html", {"context": context})
    dt_gua64, ls_gua64 = Gua.get_gua64()
    if gx.strip() in dt_gua64:
        gua_name = dt_gua64[gx.strip()]
        context = "输入卦象的卦名为：【" + gua_name + "】(上" + Gua.num_to_gua(gx[3:6]) + "下" + Gua.num_to_gua(gx[0:3]) + gua_name + ")"
        context2 = get_yao(gx, nd)
        print(context)
        #HttpResponse(s)
        return render(request, "detail.html", {"context":context, "context2":context2})

    else:
        print("输入的卦象，卦名为：未知卦")
        context = "输入的卦象，卦名为：未知卦"
        return render(request, "detail.html", {"context": context})