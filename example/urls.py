from django.conf.urls import url
from django.urls import path
#from example.views import user_list
#from example.views import log_in
from example import views 


# url(r'^sign_up/$', sign_up, name='sign_up'),
urlpatterns = [ 
    url(r'^log_in/$',views.log_in, name='log_in'),
    url(r'^log_out/$', views.log_out, name='log_out'), 
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^$', views.user_list, name='user_list'),
]

