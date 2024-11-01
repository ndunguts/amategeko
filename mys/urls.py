from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',views.user_login , name="login"),
    
    path('insertE',views.insertexam, name="insertE"),
    path('start_q/',views.start_q, name='start_q'),
    path('insert/',views.insert, name="insert"),
    path('add1/ <int:no>',views.add_tach, name='add1'),
    path('add2/', views.add_answer, name='add2'),
    path('add/',views.show_quest, name='add'),
    path('list/', views.user_detail,name='list'),
    path('test/',views.save_answer, name='test'),
    path('end/', views.end_exa, name="end" ),
    path('end_delete/',views.end_delete ,name="end_delete"),
    path('sinup/',views.sinup,name='sinup'),
    path('check/',views.check_login, name="checklogin"),
    path('out/',views.out, name="out"),
    path('correct/',views.correct, name="correct")
    
]
urlpatterns += staticfiles_urlpatterns()
