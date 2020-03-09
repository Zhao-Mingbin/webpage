from django.forms import forms
from django.shortcuts import render
from DjangoUeditor.forms import UEditorField
from .models import Article,Results,K_news,Members,Linktab

# Create your views here.

class TestUEditorForm(forms.Form):
    content = UEditorField('内容', width=600, height=600, toolbars="full", imagePath="images/", filePath="files/",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={})


# def index(request):
#     form=Article.objects
#     return render(request, 'home.html')#, {'form': form})
def home(request):
    if request.method == 'POST':
        name = request.POST['姓名']
        mail = request.POST['邮箱']
        message = request.POST['正文']
        if name and mail and message:
            contents = Linktab(name=name,mail=mail,message=message)
            contents.save()
            return render(request,'home.html',{'call_back':'恭喜提交成功，欢迎合作'})
        elif name or mail or message=='':
            return render(request, 'home.html', {'call_back': '很遗憾信息内容不全，请完善您的内容'})
    elif request.method == 'GET':
        article = Article.objects
        return  render(request,'home.html',{'homes':article})
def base(request):
    return  render(request,'base.html')
def intro(request):
    return  render(request,'intro.html')
def news(request):
    article=Article.objects
    return render(request,'news.html',{'form':article})
def news_text(request, foo_id):
    article_text=Article.objects.get(id=foo_id).content
    publish_time=Article.objects.get(id=foo_id).create_time
    name=Article.objects.get(id=foo_id).title
    return render(request, 'news_text.html', {'form':article_text,'time':publish_time,'name':name})
def results(request):
    result = Results.objects
    return  render(request,'results.html',{'result':result})
def aboutus(request):
    return  render(request,'aboutus.html')
def k_news(request):
    k_news=K_news.objects
    return  render(request,'k_news.html',{'k_news':k_news})
def k_news_text(request,foo_id):
    article_text = K_news.objects.get(id=foo_id).content
    publish_time = K_news.objects.get(id=foo_id).create_time
    name = K_news.objects.get(id=foo_id).title
    return render(request, 'k_news_text.html', {'form': article_text, 'time': publish_time, 'name': name})
def members(request):
    merbers = Members.objects
    return  render(request,'members.html',{'merbers':merbers})
def members_text(request,foo_id):
    content = Members.objects.get(id=foo_id).content
    publish_time = Members.objects.get(id=foo_id).create_time
    name = Members.objects.get(id=foo_id).name
    picture=Members.objects.get(id=foo_id).picture.url
    grade=Members.objects.get(id=foo_id).grade
    return render(request, 'member_text.html', {'content': content,
                                              'time': publish_time,
                                              'name': name,
                                                'picture':picture,
                                              'grade':grade})