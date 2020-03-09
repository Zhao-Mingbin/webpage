from django.contrib import admin
from blog.models import *
# Register your models here.





class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','name','create_time')

class LinkAdmin(admin.ModelAdmin):
	list_display =('name','mail','message')

class MembersAdmin(admin.ModelAdmin):
	list_display = ('name',  'grade','mail',)

class K_newsAdmin(admin.ModelAdmin):
	list_display = ('title','name','create_time')

class ResultsAdmin(admin.ModelAdmin):
	list_display = ('title','years','create_time','urls','content')



admin.site.register(Linktab, LinkAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Members,MembersAdmin)
admin.site.register(K_news,K_newsAdmin)
admin.site.register(Results,ResultsAdmin)