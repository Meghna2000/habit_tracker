from django.shortcuts import render
from django.views import View 
# Create your views here.
class BaseView(View):
    url_tab_navigator = {}
    base_template = 'landing.html'
    def get(self,request):
        return render(request,self.base_template)

#get_habit_related_info and get_habit_stats can be within a class based view
def get_habit_related_info(request):
    return render(request,'tracker.html')

def get_habit_stats(request):
    return render(request,'habit_stats.html')


def habit_journal(request):
    return render(request,'habit_journal.html')
