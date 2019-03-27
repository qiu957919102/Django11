from django import forms
from .models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=10,min_length=3)
    password = forms.CharField(max_length=10,min_length=3)
    password1 = forms.CharField(max_length=10,min_length=3)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password1 = cleaned_data.get('password1')
        username = cleaned_data.get('username')
        usermx = User.objects.filter(username__exact=username).first()
        if usermx != None:
            raise forms.ValidationError(message='用户存在！')

        if password != password1:
            raise forms.ValidationError(message='密码不一致！')

    class Meta:
        model = User
        fields = ['username','password']
