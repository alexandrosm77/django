# helloworld/urls.py
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from helloworld import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^new$', views.TaskNew.as_view(), name='task_new'),
    url(r'^edit/(?P<uuid>[A-Za-z0-9]+\-[A-Za-z0-9\-]+)$', views.TaskEdit.as_view(), name='task_edit'),
    url(r'^delete/(?P<uuid>[A-Za-z0-9]+\-[A-Za-z0-9\-]+)$', views.TaskDelete.as_view(), name='task_delete'),
    url(r'^mark/(?P<uuid>[A-Za-z0-9]+\-[A-Za-z0-9\-]+)$', views.TaskMark.as_view(), name='task_mark'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]

