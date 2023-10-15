from django.shortcuts import render
from django.views import View 
from .forms import *
# Create your views here.
class BaseView(View):
    url_tab_navigator = {}
    base_template = 'landing.html'
    def context_manager(self):
        #this function is to be used to get the required context variables for each page. potentially to be controlled by url information
        return

    def get(self,request):
        return render(request,self.base_template)
    

#get_habit_related_info and get_habit_stats can be within a class based view
def get_habit_related_info(request):
    return render(request,'tracker.html')

def get_habit_stats(request):
    return render(request,'habit_stats.html')


def habit_journal(request):
    return render(request,'habit_journal.html')

class HabitFormView(View):
    def get_new_habit_info(self,action):
        return
    def track_existing_habit(self,action):
        return
    def get(self,request):# ,action
        #basis the action recieved from the button click, render the required form. add that to context and display it to frontend
        form = ExistingHabitForm()
        print("habit form",form)
        return render(request, 'partials/logger_form_template.html', {
        'form': form,
    })
    def post(self,request):# ,action
        #basis the action provided submit to the respective database tables.
        return
