# 장고에서 제공되는 사용자폼 객체를 상속하여 커스터마이징한 forms.py 파일
# 여기서는 Email필드를 추가
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")