from django.conf.urls import url
from . import views


urlpatterns = [

    url('',views.index),
    url('^$',views.PostList.as_view()),
    url(r'^post/(?P<pk>\d+)$' ,views.PostDetail.as_view())]

