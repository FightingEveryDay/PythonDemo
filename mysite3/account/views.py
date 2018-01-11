from django import forms
from django.shortcuts import render_to_response
from account.models import User



# 定义表类型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名:',max_length=50)
    password = forms.CharField(label='密码:',widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件:')


# Create your views here.
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            # 将表单输入数据库
            usr = User()
            usr.username = username
            usr.password = password
            usr.email = email
            usr.save()
            # 返回注册成功页面
            return render_to_response('success.html',{'username':username})
        else:
            uf = UserForm()

        return render_to_response('registe.html',{'uf':uf})
