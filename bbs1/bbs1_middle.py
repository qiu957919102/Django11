from .models import User
from django.shortcuts import render,redirect,reverse

# 中间件 到底视图之前验证是否登录 下一步交给 装饰器
def bbs_middle(get_response):
    print('初始化')

    def middleware(request):
        user_id = request.session.get('user_id')
        userInfo = User.objects.filter(pk=user_id).first()
        if userInfo:
            #setattr把userinfo赋值给 bbs1_user
            setattr(request,'bbs1_user',userInfo)
        else:
            setattr(request,'bbs1_user',None)
        #request到达view之前的代码
        response = get_response(request)
        #到底浏览器前执行的代码
        return response
    return middleware