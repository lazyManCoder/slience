from django.contrib import admin
from apps.File.models import Note
from apps.user.models import Show
#Register your models here.

@admin.register(Note)
@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
   class Media:
         js = (
            '/static/kindeditor-master/kindeditor-all.js',#这是在后台的页面中追加js文件
             '/static/kindeditor-master/lang/zh-CN.js',
             '/static/kindeditor-master/config.js',

         )

