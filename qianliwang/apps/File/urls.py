
from django.contrib import admin
from django.urls import path,re_path,include
from django.views.static import serve
from django.conf import settings
from . import views

urlpatterns = [
    re_path('^v1/msg/$',views.Inform.as_view(),name='inform' ),
    re_path('^v1/duty/$',views.DutyStard.as_view(),name='duty' ),
    re_path('^v1/level/$',views.LevelStard.as_view(),name='level' ),
    re_path('^v1/current/$',views.Current.as_view(),name='current' ),
    re_path('^v1/msg_detail-(?P<pk>\d+).html/$',views.Detail.as_view(),name='detail' ),
    re_path('^v1/talk/$',views.Board.as_view(),name='board' ),
    re_path('^v1/api/detail/(?P<pk>\d+)/$',views.ApiDetail.as_view(),name='apidetail' ),
]
