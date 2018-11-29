from django.shortcuts import render,HttpResponse,redirect,reverse
from datetime import datetime
from blog.models import Article
from django.http import Http404

from django import forms
from django.conf import settings
# Create your views here.
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude=['pub_date','update_time']
        # error_messages = {
        #     'content': {'required': '内容不能为空'}
        # }
        widgets={
            "title": forms.widgets.TextInput(attrs={"class": "form-control"}),
            "category": forms.widgets.TextInput(attrs={"class": "form-control"}),
        }



def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'blog/home.html', {'post_list': post_list})

def add(request):
    if request.method=="GET":
        form = BlogModelForm()

        return render(request,'blog/add.html',{'form':form})
    form=BlogModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('blog:blog_home'))
    return render(request,'blog/add.html')

def delete(request,id):
    Article.objects.filter(id=id).delete()
    return redirect(reverse('blog:blog_home'))

def Test(request):
    return render(request, 'blog/test.html', {'current_time': datetime.now()})


def Detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'blog/post.html', {'post': post})
