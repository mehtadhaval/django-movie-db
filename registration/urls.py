from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    url('^login/$', auth_views.login, {'template_name': 'common/login.html'}, name='login'),
    url('^logout/$', auth_views.logout, {'template_name': 'common/logged_out.html'}, name='logout')
]