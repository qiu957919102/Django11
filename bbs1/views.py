from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.views import View
from .form import UserForm
from .models import User
from .decorators import login_deco
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_deco,name='dispatch')
class IndexView(View):
    def get(self,request):
        return render(request,'bbs1/index.html')



class RegisterView(View):
    def get(self,request):
        return render(request,'bbs1/register.html')

    def post(self,request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            err = form.errors.get_json_data()
            print(err)

            messages.info(request,err)
        return render(request,'bbs1/register.html')



class LoginView(View):
    def get(self,request):
        return render(request,'bbs1/login.html')

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        usermx = User.objects.filter(username__exact=username,password__exact=password).first()
        if usermx:
            request.session['user_id'] = usermx.id
            request.session.set_expiry(0)
            return redirect(reverse('bbs1:index'))
        else:
            messages.info(request,'帐号密码错误')
            return render(request,'bbs1/login.html')



@method_decorator(login_deco,name='dispatch')
class MusicView(View):
    def get(self,request):
        return render(request, 'bbs1/music.html')




def logout(request):
    del request.session['user_id']
    return redirect(reverse('bbs1:login'))