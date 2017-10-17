from django.conf.urls import url
from first_project import views

urlpatterns = [
    url(r'^$', views.sums, name='sums'),
    url(r'^form/', views.form_name_view, name='form name'),
    url(r'^user/', views.user, name='user')
]
