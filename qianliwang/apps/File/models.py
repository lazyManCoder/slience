from django.db import models




#留言板
class Note(models.Model):
    data = models.CharField(max_length=6000,null=True)
    create_time = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Note'
        verbose_name = '留言板'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s---%s'%(self.data,self.create_time)