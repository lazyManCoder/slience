from django.shortcuts import render,redirect,reverse,HttpResponse
from django.views import View
import time
from apps.user.summ import Summ
# Create your views here.
from apps.user import models

#首页
class Index(View):
    def get(self,request,*args,**kwargs):
        today = time.strftime("%Y-%m-%d")
        year = str(today).split('-')[0]
        month = str(today).split('-')[1]
        id = request.session.get('idcard')
        statis = Summ(id,year)
        right = statis.scount()
        if id:

            #实发工资
            salary = models.Salary_sheet.objects.filter(user__idcard=id,year=year,month=month)

            #当这个月的工资还未发放，就显示上一个月的工资
            if salary.count() > 0:
                print(salary)
                context = {
                    'salary':salary,
                    'year':year,
                    'month':month,
                    'right':right
                }
                return render(request,'index.html',context)
            else:
                month = int(month) - 1
                salary = models.Salary_sheet.objects.filter(user__idcard=id,year=year,month=month)
                context = {
                    'salary':salary,
                    'year':year,
                    'month':month
                }
                return render(request,'index.html',context)
        else:
            return render(request,'index.html')

#工资详情界面
class Detail(View):
    def get(self,request,*args,**kwargs):
        today = time.strftime("%Y-%m-%d")
        date = request.GET.get('date',today)
        year = str(date).split('-')[0]
        month = str(date).split('-')[1]
        id = request.session.get('idcard')
        if id:
            salary = models.Salary_sheet.objects.filter(user__idcard=id,year=year).all()
            return render(request,'detail.html',{'salary':salary})
        else:
            return render(request,'detail.html')



    def post(self,request,*args,**kwargs):
        date = request.POST.get('d1')
        year = str(date).split('-')[0]
        month = str(date).split('-')[1]
        id = request.session.get('idcard')
        if id:
            salary = models.Salary_sheet.objects.filter(user__idcard=id,year=year,month=month).all()
            return render(request,'detail.html',{'salary':salary})

#注册此功能尚未开启
class Register(View):
    def get(self,request,*args,**kwargs):
        return render(request,'register.html')

    def post(self,request,*args,**kwargs):
        id= request.POST.get('id')
        pwd = request.POST.get('pwd')
        obj = models.User.objects.filter(idcard=id).count()
        if obj > 0:
            models.User.objects.update_or_create(idcard=id,pwd=pwd)
        return render(request,'register.html')

#登录
class Login(View):
    def get(self,request,*args,**kwargs):
        return render(request,'login.html')

    def post(self,request,*args,**kwargs):
        idcard = request.POST.get('idcard')
        pwd = request.POST.get('pwd')
        obj = models.User.objects.filter(idcard=idcard,pwd=pwd)
        if obj:
            request.session['idcard'] = idcard

            request.session['is_login'] = True
            print(request.session)
            if request.POST.get('remember',None):
                request.session.set_expiry(100000)
            return redirect(reverse('user:index'))
        else:
            return render(request, "login.html",{'errmsg':'信息填写错误'})



#注销登录
class Logout(View):
    def get(self,request,*args,**kwargs):
        request.session.clear()
        return redirect(reverse('user:index'))


#个人信息
class User(View):
    def get(self,request,*args,**kwargs):
        idcard = request.session['idcard']
        user = models.User.objects.filter(idcard=idcard)
        return render(request,'user.html',{'user':user})