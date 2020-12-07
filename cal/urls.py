from django.conf.urls import url
from . import views

app_name= 'cal'

urlpatterns=[
    #url(r'^$', views.index, name="home"),
    url(r'^index/$', views.CalendarView.as_view(), name='index'),
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    url(r'^event/delete/(?P<event_id>\d+)/$', views.deleteEvent, name='event_delete'),
]