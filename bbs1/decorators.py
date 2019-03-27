from django.shortcuts import render,redirect,reverse
from django.contrib import messages

#中间件已经走过了，这里判断下是否为None 如果有直接返回视图，如果没 直接到的登录
def login_deco(func):
    def wrapper(request,*args,**kwargs):
        #因为有个中间件，所以在装饰器执行之前，bbs1_user其实已经赋值到 request
        #直接判断是否为None 就能判断是否登录
        if request.bbs1_user != None:
            return func(request,*args,**kwargs)
        else:
            # 如果request中没有bbs1_user说明没有通过中间件的判断
            messages.info(request,'请先登录')
            return redirect(reverse('bbs1:login'))
    return wrapper

