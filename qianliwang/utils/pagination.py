# author navigator
from django.utils.safestring import mark_safe
class Page:
    def __init__(self,current_page,data_count,per_page=6,page_num=11):
        self.current_page = current_page
        self.data_count = data_count
        self.per_page = per_page
        self.page_num = page_num

    def start(self):
        return (self.current_page - 1) * self.per_page
    def end(self):
        return self.current_page * self.per_page

    @property
    def all_count(self):
        u, y = divmod(self.data_count, self.per_page)
        if y:
            u += 1
        return u


    def page_str(self,base_url):
        page_str = []
        page_num = 9
        if self.all_count < page_num:
            start_index = 1
            end_index = self.all_count + 1
        else:
            if self.current_page <= (page_num+1)/2:
                start_index = 1
                end_index = page_num + 1
            else:
                start_index = self.current_page - (page_num-1)/2
                end_index = self.current_page + (page_num+1)/2
                if self.current_page + (page_num-1)/2 > self.all_count:
                    end_index = self.all_count + 1
                    start_index = self.all_count - page_num + 1


        if self.current_page == 1:
            prev = """<li >
                        <a href="javascript:void(0);" aria-label="Previous">
                            <span aria-hidden="true">&laquo;</span>
                        </a>
                    </li>"""
        else:
            prev = """<li >
                        <a href="%s?p=%s" aria-label="Previous">
                            <span aria-hidden="true">&laquo;</span>
                        </a>
                    </li>"""%(base_url,self.current_page-1)
        page_str.append(prev)
        for i in range(int(start_index), int(end_index)):
            if i == self.current_page:
                temp = '<li class="active"><a href="%s?p=%s">%s</a>' %(base_url,i,i)
            else:
                temp = '<li><a href="%s?p=%s">%s</a>' %(base_url,i,i)
            page_str.append(temp)
        if self.current_page == self.all_count:
            next = """<li>
                        <a href="javascript:void(0);" aria-label="Next">
                            <span aria-hidden="true">&raquo;</span>
                        </a>
                    </li>"""
        else:
            next = """<li>
                        <a href="%s?p=%s" aria-label="Next">
                            <span aria-hidden="true">&raquo;</span>
                        </a>
                    </li>"""%(base_url,self.current_page+1)
        page_str.append(next)

        jump = """
            <span class="turn">
            <input id="t1" type="text" /><a onclick='jumpTo(this,"%s?p=");'>GO</a>
            </span>
        """%(base_url)
        page_str.append(jump)
        page_str = "".join(page_str)
        page_str = mark_safe(page_str)
        return page_str