from django.conf.urls import url
from first_project import views

urlpatterns = [
    url(r'^$', views.sums,name='sums')
]