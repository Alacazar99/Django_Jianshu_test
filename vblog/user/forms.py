from django import forms
from .models import User
import hashlib

# class RegisterForm(forms.Form):
#     username = forms.CharField(label="用户名", required=True,min_length=4,error_messages={'required':"用户名不能为空",'min_length':"用户名最少4个字符"})
#     password = forms.CharField(label="密码", required=True, min_length=6,error_messages={'required':"密码不能为空",'min_length':"密码最少6个字符"})
#     email = forms.EmailField(label="邮箱", required=True ,error_messages={'required':"邮箱不能为空"})
#     valid_code = forms.CharField(label="验证码",required=True,error_messages={"required":"验证码不能为空"})


class RegisterForm(forms.ModelForm):
    user_name = forms.CharField(label="用户名", required=True, min_length=4, error_messages={'required': "用户名不能为空", 'min_length': "用户名最少4个字符"})
    password = forms.CharField(widget=forms.PasswordInput ,label="密码", required=True, min_length=6, error_messages={'required': "密码不能为空", 'min_length': "密码最少6个字符"})
    re_password = forms.CharField(widget=forms.PasswordInput ,label="确认密码", required=True, min_length=6, error_messages={'required': "确认密码不能为空", 'min_length': "密码最少6个字符"})
    email = forms.EmailField(label="邮箱", required=True, error_messages={'required': "邮箱不能为空"})
    valid_code = forms.CharField(label="验证码", required=True, error_messages={"required": "验证码不能为空"})



    class Meta:
        model = User
        fields = ['user_name','password','re_password','email','valid_code']

    def clean_valid_code(self):
        valid_code = self.cleaned_data.get('valid_code')

        if (valid_code != self.s_valid_code):
            return self.add_error('valid_code',"验证码不正确")

    def set_session_validcode(self,s_valid_code):
        """传入session中的验证码"""
        self.s_valid_code = s_valid_code

    def clean(self):
        super().clean()
        """验证两次输入是否相同"""
        clean_data = self.cleaned_data
        password = clean_data.get('password')
        re_password = clean_data.get("re_password")

        if password != re_password :
            print(password,'--',re_password)
            return self.add_error("re_password","两次密码输入不一致")


class LoginForm(forms.Form):
    user_name = forms.CharField(label="用户名", required=True, min_length=4, error_messages={'required': "用户名不能为空", 'min_length': "用户名最少4个字符"})
    password = forms.CharField(widget=forms.PasswordInput, label="密码", required=True, min_length=6,error_messages={'required': "密码不能为空", 'min_length': "密码最少6个字符"})