from . import models

class Summ:
    def __init__(self,id,year):
        self.id = id
        self.year = year


    def scount(self):
        salary = models.Salary_sheet.objects.filter(user__idcard=self.id,year=self.year).all()
        #应发
        should_send = 0
        #实发
        real_send = 0
        #补发
        rei = 0
        #财政扣款
        fis = 0
        for row in salary:
            should_send += int(row.should)
            print(row.salary_pay)
            real_send += float(row.salary_pay)
            rei += int(row.reissue)
            fis += int(row.fiscal)

        return should_send,real_send,rei,fis


