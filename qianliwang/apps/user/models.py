from django.db import models
from django.urls import reverse

#模型类
class BaseModel(models.Model):
    #说明
    explain = models.CharField(max_length=32)
    #执行时间
    time0 = models.CharField(max_length=32)
    #备注
    remark = models.CharField(max_length=32)
    #当前状态
    current = models.CharField(max_length=32)

    #起算时间
    start = models.CharField(max_length=32,null=True)
    #截至时间
    end = models.CharField(max_length=32,null=True)

    #依据文件
    accord = models.CharField(max_length=32,null=True)



    class Meta:
        abstract = True

#工号身份证对照表
class User(models.Model):
    #人员编号
    staff = models.IntegerField(default='1',null=True)

    #密码
    pwd = models.CharField(max_length=32,null=True,default='888888')

    #姓名
    name = models.CharField(max_length=32,null=True)

    #头像
    headimg = models.ImageField(upload_to='icon',default='icon/default.jpg')

    #对接工资卡号中的信息
    # msg = models.ForeignKey("Salary_sheet",on_delete=True,null=True)

    #工资卡号
    wage_card = models.CharField(max_length=32)
    #序号
    seq = models.CharField(max_length=32)
    #开资单位
    open = models.CharField(max_length=32)
    #身份证号
    idcard = models.CharField(max_length=18,null=True)
    #人员状态
    status = models.CharField(max_length=32)
    #备注
    remark = models.CharField(max_length=64)
    #查询隶属单位
    unit = models.CharField(max_length=32)
    #勤务隶属单位
    service = models.CharField(max_length=32)

    class Meta:
        db_table = 'User_detail'
        verbose_name = '工资卡号信息集'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s'%self.name




#工资发放信息说明表
class Send(models.Model):
    mine = models.ForeignKey("User",on_delete=True)
    #备注
    remark = models.CharField(max_length=64)
    #工资变动说明
    change = models.CharField(max_length=64)
    #年度
    year = models.IntegerField()
    #月份
    month = models.IntegerField()

    class Meta:
        db_table = 'Salary_change'
        verbose_name = '工资发放信息说明表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<%s>-<%s>'%(self.mine.name,self.change)




#工资条
class Salary_sheet(models.Model):

    user = models.ForeignKey("User",on_delete=True,null=True)
    #职务工资
    duty = models.CharField(max_length=32,null=True)
    #级别工资
    level = models.CharField(max_length=32,null=True)
    #岗位工资
    station = models.CharField(max_length=32,null=True)
    #薪级工资
    salary_post = models.CharField(max_length=32,null=True)
    #技术等级工资
    tcgrade = models.CharField(max_length=32,null=True)
    #教师10%工资
    teacher = models.CharField(max_length=32,null=True)
    #警衔补贴
    police_rank = models.CharField(max_length=32,null=True)
    #行业津补贴
    industry = models.CharField(max_length=32,null=True)


    #伤残补助
    maim = models.CharField(max_length=32,null=True)
    #津贴
    allowance = models.CharField(max_length=32,null=True)
    #特殊补助
    special = models.CharField(max_length=32,null=True)
    #取暖费
    heart = models.CharField(max_length=32,null=True)
    #独生子女
    only_child = models.CharField(max_length=32,null=True)
    #电话费
    phone_fee = models.CharField(max_length=32,null=True)
    #现行补贴
    current_subsiby = models.CharField(max_length=32,null=True)
    #公务交通补贴
    traffic = models.CharField(max_length=32,null=True)
    #其他一
    others = models.CharField(max_length=32,null=True)
    #硕博补贴
    thurber = models.CharField(max_length=32,null=True)
    #补发工资
    reissue = models.CharField(max_length=32,null=True)
    #其他2
    other2 = models.CharField(max_length=32,null=True)
    #个人基本养老保险金
    individual = models.CharField(max_length=32,null=True)
    #财政扣款
    fiscal = models.CharField(max_length=32,null=True)
    #职业年金
    profession = models.CharField(max_length=32,null=True)
    #应发项
    should = models.CharField(max_length=32,null=True)
    #所得税
    income = models.CharField(max_length=32,null=True)
    #住房基金
    house = models.CharField(max_length=32,null=True)

    #失业保险
    lose = models.CharField(max_length=32,null=True)
    #医疗保险
    hospital = models.CharField(max_length=32,null=True)
    #扣款合计
    combined = models.CharField(max_length=32,null=True)
    #扣款其他项目一
    other_item = models.CharField(max_length=32,null=True)
    #扣款其他项目二
    other_item1 = models.CharField(max_length=32,null=True)
    #实发工资
    salary_pay = models.CharField(max_length=32,null=True)
    #年份
    year = models.IntegerField(null=True)
    #月份
    month = models.IntegerField(null=True)

    class Meta:
        db_table = 'Salary_sheet'
        verbose_name = '市政统发工资表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<%s>-<%s>'%(self.duty,self.level)

#级别工资发放标准表
class Level(BaseModel):

    #工资标准
    wage_level = models.CharField(max_length=32)
    #序号
    seq = models.CharField(max_length=32)
    #级别档次
    grade = models.CharField(max_length=32)


    class Meta:
        db_table = 'Salary_Level'
        verbose_name = '级别工资发放标准表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<%s>-<%s>'%(self.grade,self.wage_level)

#职务工资发放标准表
class Duty(BaseModel):

    #工资标准
    wage_level = models.CharField(max_length=32)
    #序号
    seq = models.CharField(max_length=32)
    #职务名称
    duty = models.CharField(max_length=32)
    #职务序列
    duty_seq = models.CharField(max_length=32)


    class Meta:
        db_table = 'Salary_Duty'
        verbose_name = '职务工资发放标准表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<%s>-<%s>'%(self.duty,self.wage_level)



#警衔工资发放标准表
class Police_rank(BaseModel):
    #发放标准
    sent = models.CharField(max_length=32)
    #序号
    seq = models.CharField(max_length=32)
    #警衔名称
    police = models.CharField(max_length=32)

    class Meta:
        db_table = 'Police_rank'
        verbose_name = '警衔工资发放标准表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<%s>-<%s>'%(self.sent,self.police)

#现行补贴发放标准
class Current_sub(BaseModel):
    #职务名称
    duty = models.CharField(max_length=32,null=True)
    #发放标准
    sent = models.CharField(max_length=32)



    class Meta:
        db_table = 'Current_sub'
        verbose_name = '现行补贴发放标准'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<%s>-<%s>'%(self.sent,self.file)


#公务交通补贴发放标准
class Traffic(BaseModel):
    #发放标准
    sent = models.CharField(max_length=32)
    #文件依据
    file = models.CharField(max_length=32)
    #发文时间
    time1 = models.CharField(max_length=32)
    #废止时间
    end = models.CharField(max_length=32)
    #职务级别
    level = models.CharField(max_length=32)

    class Meta:
        db_table = 'Traffic'
        verbose_name = '公务交通补贴发放标准'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<%s>-<%s>'%(self.sent,self.file)



# Create your models here.
class Show(models.Model):
    # cover = models.ImageField(upload_to='icon',default='icon/default.jpg')
    title = models.CharField(max_length=32,null=True)
    content = models.TextField('内容',blank=True)
    create_time = models.DateField(auto_now_add=True,null=True)
    views = models.PositiveIntegerField('浏览量',default=0)

    class Meta:
        db_table = 'Show'
        verbose_name = '通知/通告/公示'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s ---- %s  -----%s'%(self.content,self.views,self.comment_set)

    def get_absolute_url(self):
        return reverse('file:detail',args=[str(self.id)])

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])


#现行工资标准



#发表评论表
class Comment(models.Model):
    #姓名
    msg = models.ForeignKey("User",on_delete=True,null=True)

    #内容
    content = models.CharField(max_length=255,null=True)

    #创建的时间
    create_time = models.DateTimeField(auto_now_add=True)



    class Meta:
        db_table = 'Comment'
        verbose_name = '留言板上的说说'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<%s>-<%s>'%(self.msg,self.content)

#回复评论
class reply(models.Model):
    #回复的时间
    tim = models.DateTimeField(auto_now_add=True)

    #回复的内容
    data = models.CharField(max_length=255)

    #标识的uid,目的不止一个人评论
    # uid = models.CharField(max_length=32,null=True)

    #身份
    user = models.ForeignKey("User",on_delete=True)

    #回复id，与reply进行关联
    comment = models.ForeignKey("Comment",on_delete=True,null=True)
    class Meta:
        db_table = 'reply'
        verbose_name = '回复的信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '<%s>-<%s>'%(self.user,self.data)
