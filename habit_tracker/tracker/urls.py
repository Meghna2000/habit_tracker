from django.urls import path,include
import tracker.views as views
#from tracker.views import BaseView
app_name = 'tracker'
urlpatterns = [
    path('',views.BaseView.as_view(),name='base_view'),
    path('tracker',views.get_habit_related_info,name='habit_info'),
    path('journal',views.habit_journal,name='habit_journal'),
    path('habit_form',views.HabitFormView.as_view(),name='habit_form')
    
]
