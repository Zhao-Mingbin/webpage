from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
#氢能资讯
class Article(models.Model):
    name = models.CharField(default='氢安全',max_length=100, verbose_name='作者')
    title = models.CharField(max_length=100, verbose_name='标题')

    content = UEditorField(width=1200, height=300, toolbars="full", imagePath="images/", filePath="files/",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={}, verbose_name='内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')

    class Meta:
        db_table = 'Article'
        verbose_name = '氢能资讯'
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.title
#课题组新闻
class K_news(models.Model):
    name = models.CharField(default='氢安全',max_length=100, verbose_name='作者')
    title = models.CharField(max_length=100, verbose_name='标题')

    content = UEditorField(width=1200, height=300, toolbars="full", imagePath="images/", filePath="files/",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={}, verbose_name='内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')

    class Meta:
        db_table = 'K_news'
        verbose_name = '课题组新闻'
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.title
#成员介绍
class Members(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    mail = models.CharField(default='请输入邮箱地址',max_length=100, verbose_name='邮箱')
    grade = models.CharField(default='请输入年级（硕士/博士/老师）',max_length=100, verbose_name='年级')
    picture = models.ImageField(upload_to="images/",verbose_name='照片')
    content = UEditorField(width=1200, height=300, toolbars="full", imagePath="images/", filePath="files/",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={}, verbose_name='内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'Members'
        verbose_name = '成员介绍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
#研究成果
class Results(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')

    content = models.CharField(max_length=500, verbose_name='内容')
    urls = models.CharField(default='www',max_length=100, verbose_name='链接')
    years = models.CharField(max_length=100, verbose_name='成果时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')

    class Meta:
        db_table = 'Results'
        verbose_name = '研究成果'
        verbose_name_plural = verbose_name
    def __str__(self):
        return  self.title
#联系方式
class Linktab(models.Model):
    name = models.CharField(max_length=100,verbose_name='姓名')
    mail = models.CharField(max_length=100,verbose_name='邮箱')
    message = models.CharField(max_length=1000,verbose_name='信息')
    class Meta:
        db_table = 'Linktab'
        verbose_name = '联系方式'
        verbose_name_plural = verbose_name
        verbose_name = ''
    def __str__(self):
        return  self.name