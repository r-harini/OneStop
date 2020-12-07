
from django.conf.urls import url
from . import views

app_name= 'todo'
urlpatterns = [
    url(r'^$',views.index, name="index"),
    url(r'^update_task/(?P<pk>\w+)/$', views.updateTask, name="update_task"),
   url(r'^delete/(?P<pk>\w+)/$', views.deleteTask, name="delete_task"),

]