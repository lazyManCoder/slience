from django.contrib import admin

# Register your models here.
from apps.user.models import User,Salary_sheet


admin.site.site_title = '四平市公安局财政统发工资查询系统后台管理'
admin.site.site_header = '四平市公安局财政统发工资查询系统后台管理'



admin.site.register(Salary_sheet)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','staff','wage_card','seq','open','idcard','status','remark','unit','service','pwd']
