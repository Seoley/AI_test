
from django import forms

# https://velog.io/@zihs0822/Form-%EC%9D%B4%EB%9E%80
# https://nalara12200.tistory.com/172
class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        label="사용자 이름",
        max_length=32
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="비밀번호",
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        }
    )
