from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('user/',views.userreg, name='user'),
    path('insert/',views.insert, name="insert"),
    path('add1/ <int:id>',views.add_tach, name='add1'),
    path('add2/', views.add_answer, name='add2'),
    path('add/',views.show_quest, name='add'),
    path('list/', views.user_detail,name='list'),
    path('test/',views.save_answer, name='test')
]
urlpatterns += staticfiles_urlpatterns()
