from django.conf.urls import url
from sampling import views

urlpatterns = [
    # 書籍
    url(r'^umakihon/$', views.uma_kihon_list, name='uma_kihon_list'),   # 一覧
    url(r'^umakihon/add/$', views.uma_kihon_edit, name='uma_kihon_add'),  # 登録
    url(r'^umakihon/mod/(?P<uma_kihon_id>\d+)/$', views.uma_kihon_edit, name='uma_kihon_mod'),  # 修正
    url(r'^umakihon/del/(?P<uma_kihon_id>\d+)/$', views.uma_kihon_del, name='uma_kihon_del'),   # 削除
    #番組
    url(r'^bangumi/$', views.bangumi_list, name='bangumi_list'),   # 一覧
    #直前情報
    url(r'^tyokuzen/$', views.tyokuzen_list, name='tyokuzen_list'),   # 一覧
    #前走
    url(r'^zensou/$', views.zensou_list, name='zensou_list'),   # 一覧
    #騎手
    url(r'^kishu_sabun/$', views.kishu_sabun_list, name='kishu_sabun_list'),   # 一覧
               
]
