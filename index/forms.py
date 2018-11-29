from django import forms
from index import models
from django.core.exceptions import ValidationError


# class RegForm(forms.Form):
#  自己写字段
#     username = forms.CharField(
#         label='用户名'
#     )
#     password = forms.CharField(
#         label='密码',
#         widget=forms.widgets.PasswordInput()
#     )
#     re_password = forms.CharField(
#         label='确认密码',
#         widget=forms.widgets.PasswordInput()
#     )
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for filed in self.fields.values():
#             filed.widget.attrs.update({"class": "form-control"})
#
#     def clean(self):
#         if self.cleaned_data.get('password') != self.cleaned_data.get('re_password'):
#             self.add_error('re_password', '两次密码不一致')
#             raise ValidationError('两次密码不一致')
#         return self.cleaned_data


class RegForm(forms.ModelForm):
    # 引用models.py UserInfo中的字段,没有的再进行补充
    re_password = forms.CharField(label='确认密码', min_length=6,
                                  widget=forms.widgets.PasswordInput(attrs={"class": 'form-control'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed in self.fields.values():
            filed.widget.attrs.update({"class": "form-control"})

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('re_password'):
            self.add_error('re_password', '两次密码不一致')
            raise ValidationError('两次密码不一致')
        return self.cleaned_data

    class Meta:
        model = models.UserInfo
        fields = ['username',  'password', 're_password']
        labels = {
            'username': '用户名',
            'name': '真实姓名',
            'password': '密码',
            're_password': '确认密码',
        }
        error_messages = {
            'username': {
                'required': '必填',
                'min_length': '最小长度为6个'

            },
            're_password': {
                'min_length': '最小长度为6个'
            }
        }
        widgets = {
            'password': forms.widgets.PasswordInput(attrs={"class": 'form-control'}),
        }
