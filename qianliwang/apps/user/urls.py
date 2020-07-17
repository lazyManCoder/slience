
from django.contrib import admin
from django.urls import path,re_path,include
from user import views
urlpatterns = [

    re_path('^$',views.Login.as_view(),name='login' ),
    re_path('^v1/user/register/$',views.Register.as_view(),name='register' ),
    re_path('^v1/user/detail/$',views.Detail.as_view(),name='detail' ),
    re_path('^v1/user/logout/$',views.Logout.as_view(),name='logout' ),
    re_path('^v1/user/user/$',views.User.as_view(),name='user' ),
    re_path('^index/$',views.Index.as_view(),name='index' ),
]
