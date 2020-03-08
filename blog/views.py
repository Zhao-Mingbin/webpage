from django.forms import forms
from django.shortcuts import render
from DjangoUeditor.forms import UEditorField
from .models import Article

# Create your views here.

class TestUEditorForm(forms.Form):
    content = UEditorField('内容', width=600, height=600, toolbars="full", imagePath="images/", filePath="files/",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={})


# def index(request):
#     form=Article.objects
#     return render(request, 'home.html')#, {'form': form})
def home(request):
    return  render(request,'home.html')
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