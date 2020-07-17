from django.shortcuts import render,reverse,HttpResponse
from django.views import View
from apps.File.models import Note
from apps.user.models import Comment,Show,User,Duty,Level,Current_sub,reply
from utils.pagination import Page
from django.views.generic import DetailView
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.serializer import BookSerializer
# Create your views here.
#公示界面
class Inform(View):
    def get(self,request,*agrs,**kwargs):
        LIST = []
        msg = Show.objects.order_by("-create_time")
        for i in msg:
            LIST.append(i)
        current_page = request.GET.get('p',1)
        current_page = int(current_page)
        page_obj = Page(current_page,len(LIST))
        comments = 1
        data = LIST[page_obj.start():page_obj.end()]
        context = {
            'msg':msg,
            'content_all': data,
            'page_str':page_obj.page_str(reverse('file:inform')),
            'comments':comments
        }

        return render(request,'inform.html',context)



#浏览器的点击次数
class Detail(DetailView,View):
    model = Show
    template_name = 'user/show_detail.html'
    context_object_name = 'show'
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.viewed()
        return obj


class ApiDetail(APIView):
    def get(self,request,*agrs,**kwargs):
        id = kwargs.get('pk')
        comment = Comment.objects.filter(article=id)

        ser = BookSerializer(comment,many=True)
        print(ser.data)
        return Response({'res':ser.data})


    # def post(self,request,*agrs,**kwargs):
    #     id = kwargs.get('pk')
    #     data = request.POST.get('data')
    #     idcard = request.session.get('idcard')
    #     user = User.objects.filter(idcard=idcard)
    #     user_id = [i.id for i in user]
    #     comment = Comment.objects.filter(article=id).create(content=data,msg_id=user_id[0],article_id=id)
    #     context = {
    #         'comment':comment,
    #         'status':200
    #     }
    #
    #     return HttpResponse(context)


#留言评论和回复功能
class Board(View):
    def get(self,request,*args,**kwargs):
        idcard = request.session.get('idcard')
        user = User.objects.filter(idcard=idcard)
        comment = Comment.objects.order_by("-create_time")

        reply_data = reply.objects.all()
        # comment_num = reply.objects.filter(comment_id=reply_num).count()
        context = {
            'user':user,
            'comment':comment,
            'reply':reply_data,
             # 'comment_num':comment_num
        }
        return render(request,'board.html',context)

    def post(self,request,*args,**kwargs):
        #发送说说的内容
        data = request.POST.get('data')
        print(data)
        #发送回复的数据
        reply_data = request.POST.get('reply_data')
        print(reply_data)
        idcard = request.session.get('idcard')
        user = User.objects.filter(idcard=idcard)
        user_id = [i.id for i in user]

        reply_num = request.POST.get('num')
        #comment需要的元素是知道姓名是谁，思路可以通过身份证号找到那个
        if data != None:
            print('hello')
            comment = Comment.objects.filter(msg__idcard=idcard).create(msg_id=user_id[0],content=data)
        else:
            comment = Comment.objects.filter(msg__idcard=idcard)
        if reply_data != None:
            reply_data = reply.objects.filter(user__idcard=idcard).create(data=reply_data,user_id=user_id[0],comment_id=reply_num)



        context = {
            'comment':comment,
            'reply':reply_data,

        }
        print(context)
        return HttpResponse(context)


#职务工资标准
class DutyStard(View):
    def get(self,request,*args,**kwargs):
        res = Duty.objects.all()
        context = {
            'res':res
        }
        return render(request,'duty.html',context)




#级别等级工资
class LevelStard(View):
    def get(self,request,*args,**kwargs):
        res = Level.objects.all()
        context = {
            'res':res
        }
        return render(request,'level.html',context)



#现行补贴发放标准
class Current(View):
    def get(self,request,*args,**kwargs):
        res = Current_sub.objects.all()
        context = {
            'res':res
        }
        return render(request,'current.html',context)


