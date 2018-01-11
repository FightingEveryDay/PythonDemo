from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'^$', views.register, name='register'),
    url(r'^register/$',views.register,name = 'register'),
]